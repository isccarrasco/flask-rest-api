from datetime import datetime

from backend import db


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    city = db.Column(db.String(50))

    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __repr__(self):
        return '<Team: %s - % s>' % (self.name, self.city)


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    number = db.Column(db.Text)
    birth_date = db.Column(db.DateTime)

    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team = db.relationship('Team', backref=db.backref('players', lazy='dynamic'))

    def __init__(self, name, number, team, birth_date=None):
        self.name = name
        self.number = number
        if birth_date is None:
            birth_date = datetime.utcnow()
        self.birth_date = birth_date
        self.team = team

    def __repr__(self):
        return '<Player %r>' % self.name

