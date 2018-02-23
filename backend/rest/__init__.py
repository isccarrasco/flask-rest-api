import logging
import traceback

from flask import Blueprint
from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound

import settings

log = logging.getLogger(__name__)

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(
    app=api_blueprint,
    version='1.0.0',
    title='My Flask, Blueprint, Flask-RESTPlus and Swagger API Example',
    description='''This is an example developed to show how can we configure a
        REST API using Flask as a main backend framework, adding Blueprint
        to organize the application, Flask-RESTPlus to configure the REST
        dispatchers and Swagger for documenting the API''',
    contact='@isccarrasco',
    contact_url='http://twitter.com/isccarrasco',
    contact_email="mario.carrasco@gmail.com"
)


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404

