import logging

from flask import current_app as app

log = logging.getLogger(__name__)


class ExampleModel():

    def get(self):
        return {'foo': 'bar'}
