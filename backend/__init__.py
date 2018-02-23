from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('settings')

db = SQLAlchemy(app)


from backend.rest import api, api_blueprint
from backend.rest.endpoints.teams import ns_team
from backend.rest.endpoints.players import ns_player

api.add_namespace(ns_team)
api.add_namespace(ns_player)
app.register_blueprint(blueprint=api_blueprint)


from backend.site.routes import site_blueprint
app.register_blueprint(blueprint=site_blueprint)


from backend.database.models import Team

db.drop_all()
db.create_all()