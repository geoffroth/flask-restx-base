import logging

from flask_restx import Namespace, Resource, fields
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from __version__ import __version__
from server.api.models.example_model import ExampleModel
from server.api.schema.example_schema import schema as example_schema

log = logging.getLogger(__name__)

api = Namespace('example', description='Retrieve example')

columns = {
    'items': fields.Raw
}

model = api.model('Example', columns)


@api.route('/')
@api.doc()
class ExampleList(Resource):
    @api.doc('example')
    @api.marshal_list_with(model)
    def get(self, site=None):
        """ Example """
        # try:
        #     validate(instance=example, schema=example_schema)
        # except ValidationError as err:
        #     log.exception(err.message)
        #     return api.abort(400, "Invalid example")

        response = ExampleModel().get()
        return {
            'items': dict(response)
        }
