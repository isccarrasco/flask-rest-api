import logging.config

from backend import app
from settings import FLASK_DEBUG

logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)

if __name__ == '__main__':
    log.info('>>>>> Starting server <<<<<')
    app.run(debug=FLASK_DEBUG)
