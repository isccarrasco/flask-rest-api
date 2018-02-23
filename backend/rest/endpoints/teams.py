import logging

from flask import request
from flask_restplus import Namespace, Resource

from backend.database.models import Team
from backend.rest.endpoints.business import create_team, update_team, delete_team
from backend.rest.endpoints.serializers import team, team_with_players

log = logging.getLogger(__name__)

ns_team = Namespace(name='teams', description='Describes the operations related with the teams')


@ns_team.route('/')
class TeamCollection(Resource):

    @ns_team.marshal_list_with(team)
    def get(self):
        """
        Returns a list of teams.
        Use this method to get the list of teams stored on the database.
        """
        teams = Team.query.all()
        return teams

    @ns_team.response(201, 'Team successfully created.')
    @ns_team.expect(team)
    def post(self):
        """
        Creates a new team.
        Use this method to create a new element on the team table of the database.
        * Send a JSON object with the new name and the city (required) in the request body.
        ```
        {
            "name": "Yankees",
            "city": "New York"
        }
        ```
        """
        data = request.json
        create_team(data)
        return None, 201


@ns_team.route('/<int:id>')
@ns_team.response(404, 'Team not found.')
class TeamItem(Resource):

    @ns_team.marshal_with(team_with_players)
    def get(self, id):
        """
        Returns a team with a players list
        Use this method to get a team with the list of players of the team
        """
        return Team.query.filter(Team.id == id).one()

    @ns_team.expect(team)
    @ns_team.response(204, 'Team successfully updated.')
    def put(self, id):
        """
        Updates the data of a team.
        Use this method to change the name or city for a baseball team.
        * Send a JSON object with the new name and/or the city in the request body.
        ```
        {
          "name": "Cubs",
          "city": "Chicago"
        }
        ```
        * Specify the ID of the team to modify in the request URL path.
        """
        data = request.json
        update_team(id, data)
        return None, 204

    @ns_team.response(204, 'Team successfully deleted.')
    def delete(self, id):
        """
        Deletes an existing team.
        Use this method to delete a team from the database
        * Send the ID of the team you want to delete
        """
        delete_team(id)
        return None, 204