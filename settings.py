# Flask settings
FLASK_DEBUG = True  # Do not use debug mode in production

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = True


# Flask-Restplus settings
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
ERROR_404_HELP = False
