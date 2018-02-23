from flask_restplus import fields

from backend.rest import api

team = api.model('Baseball Team', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a team'),
    'name': fields.String(required=True, description='Team name'),
    'city': fields.String(required=True, description='City where the team reside')
})

team_players = api.model('Baseball players', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a player'),
    'name': fields.String(required=True, description='Player name'),
    'number': fields.String(required=True, description='Player number'),
    'birth_date': fields.DateTime,
    'team_id': fields.Integer(attribute='team.id'),
    'team': fields.String(attribute='team.id'),
})

team_with_players = api.inherit('Baseball team with players', team, {
    'players': fields.List(fields.Nested(team_players))
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_players = api.inherit('Page of players', pagination, {
    'items': fields.List(fields.Nested(team_players))
})