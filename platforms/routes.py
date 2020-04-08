import json

from flask import Blueprint, request
from flask_restful import Resource, reqparse
from flask_security.decorators import auth_token_required, login_required
from flask_security import current_user
from flask_sse import sse
from platforms import api

bp = Blueprint('main', __name__)

parser = reqparse.RequestParser()
parser.add_argument('message')
parser.add_argument('channel')
parser.add_argument('type')


class SendMessage(Resource):
    @auth_token_required
    def post(self):
        parsed_args = parser.parse_args()
        message = parsed_args['message']
        channel = parsed_args['channel']
        type_message = parsed_args['type']
        if all([message, channel, type_message]):
            sse.publish(message, type=type_message, channel=channel)
            return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
        return json.dumps({'success': False}), 404, {'ContentType': 'application/json'}

    @login_required
    def get(self):
        if int(current_user.id) == int(request.args.get('user_id')):
            return {'token': current_user.get_auth_token()}
        else:
            return {'token': "Just go away!!!"}


api.add_resource(SendMessage, '/send')
api.add_resource(SendMessage, '/token', endpoint="api.token_gen")
