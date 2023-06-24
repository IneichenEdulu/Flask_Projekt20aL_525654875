from flask import request
from models.user import User
from flask_restful import Resource
from http import HTTPStatus
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required  # noqa: E501

class TokenResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.get_by_username(username)

        if not user or not User.verify_password(password, user.password):
            return {'message': 'username or password is incorrect'}, 
        HTTPStatus.UNAUTHORIZED
        
        return {'access_token': create_access_token(identity=user.id, fresh=True),
                'refresh_token': create_refresh_token(identity=user.id)}, HTTPStatus.OK
    
class RefreshResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        return {'access_token': create_access_token(identity=current_user, fresh=False)}, HTTPStatus.OK  # noqa: E501