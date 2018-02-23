from backend import db
from backend.database.models import Team, Player


def create_team(data):
    team_id = data.get('id')
    name = data.get('name')
    city = data.get('city')

    team = Team(name, city)
    if team_id:
        team.id = team_id

    db.session.add(team)
    db.session.commit()


def update_team(team_id, data):
    team = Team.query.filter(Team.id == team_id).one()
    team.name = data.get('name')
    team.city = data.get('city')
    db.session.add(team)
    db.session.commit()


def delete_team(team_id):
    team = Team.query.filter(Team.id == team_id).one()
    db.session.delete(team)
    db.session.commit()


def create_player(data):
    name = data.get('name')
    number = data.get('number')
    team_id = data.get('team_id')
    team = Team.query.filter(Team.id == team_id).one()
    player = Player(name, number, team)
    db.session.add(player)
    db.session.commit()


def update_player(player_id, data):
    player = Player.query.filter(Player.id == player_id).one()
    player.name = data.get('name')
    player.number = data.get('number')
    team_id = data.get('team_id')
    player.team = Team.query.filter(Team.id == team_id).one()
    db.session.add(player)
    db.session.commit()


def delete_player(player_id):
    player = Player.query.filter(Player.id == player_id).one()
    db.session.delete(player)
    db.session.commit()