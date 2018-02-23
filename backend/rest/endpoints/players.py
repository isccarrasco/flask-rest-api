import logging

from flask import request
from flask_restplus import Namespace, Resource

from backend.database.models import Player
from backend.rest.endpoints.business import create_player, update_player, delete_player
from backend.rest.endpoints.parsers import pagination_arguments
from backend.rest.endpoints.serializers import page_of_players, team_players

log = logging.getLogger(__name__)

ns_player = Namespace('players', description='Operations related with the players of a team')


@ns_player.route('/')
class PlayerCollection(Resource):

    @ns_player.expect(pagination_arguments)
    @ns_player.marshal_with(page_of_players)
    def get(self):
        """
        Returns list of players.
        Use this methods to get the list of players stored on the database and the team related.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        players_query = Player.query
        players_page = players_query.paginate(page, per_page, error_out=False)

        return players_page

    @ns_player.expect(team_players)
    def post(self):
        """
        Creates a new player.
        Use this method to create a new element on the player table of the database linked with a team
        * Send a JSON object with the data of the new player in the request body
        ```
        {
            "name": "Derek Jeter",
            "numbre": "2",
            "birth_date": "1975-06-26",
            "team_id": 1
        }
        ```
        """
        create_player(request.json)
        return None, 201


@ns_player.route('/<int:id>')
@ns_player.response(404, 'Player not found.')
class PlayerItem(Resource):

    @ns_player.marshal_with(team_players)
    def get(self, id):
        """
        Returns the data of a player.
        Use this method to get a player record with the team related
        * Send the ID as a parameter
        """
        return Player.query.filter(Player.id == id).one()

    @ns_player.expect(team_players)
    @ns_player.response(204, 'Player successfully updated.')
    def put(self, id):
        """
        Updates the data of a player.
        Use this method to change the data about a player
        * Send a JSON object with the data you want to change
        ```
        {
          "name": "Derek Jeter",
          "number": "2"
          "birth_date": "1974-06-26",
          "team_id": 1
        }
        ```
        """
        data = request.json
        update_player(id, data)
        return None, 204

    @ns_player.response(204, 'Player successfully deleted.')
    def delete(self, id):
        """
        Deletes player.
        Use this method to erase a player from the database
        * Send the ID of the player you want to delete
        """
        delete_player(id)
        return None, 204


@ns_player.route('/ages/<int:year>/')
@ns_player.route('/ages/<int:year>/<int:month>/')
@ns_player.route('/ages/<int:year>/<int:month>/<int:day>/')
class PlayerArchiveCollection(Resource):

    @ns_player.expect(pagination_arguments, validate=True)
    @ns_player.marshal_with(page_of_players)
    def get(self, year, month=None, day=None):
        """
        Returns a list of players who were born in a specified time period.
        Use this method to get a list of players who were born in a time period gived as a parameter
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        start_month = month if month else 1
        end_month = month if month else 12
        start_day = day if day else 1
        end_day = day + 1 if day else 31
        start_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, start_month, start_day)
        end_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, end_month, end_day)
        players_query = Player.query.filter(Player.birth_date >= start_date).filter(Player.birth_date <= end_date)

        players_page = players_query.paginate(page, per_page, error_out=False)

        return players_page
