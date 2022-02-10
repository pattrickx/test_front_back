from wsgiref.simple_server import server_version
from flask import Flask, request, jsonify, make_response, session
from flask_session import Session
from flask_cors import CORS, cross_origin
import jwt
import datetime
from functools import wraps
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
app.config['SESSION_TYPE'] = 'filesystem'
# app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, supports_credentials=True)
server_version = Session(app)
# app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': "token is missing!"}),401

        try: 
            data = jwt.decode(token,app.secret_key)
            current_user = "current_user"
        except:
            return jsonify({'message': "token is invalid!"}),401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

def create_app(testing: bool = True):
    
    # @cross_origin
    @app.route("/hello")
    @token_required
    def test(current_user):
        return f"HELLO token"
    # @cross_origin(supports_credentials=True)
    @app.route("/user") 
    def user():
        print(request.cookies)
        user_id = session.get('user_id')
        print(user_id)
        print(session)
        if not user_id:
            return jsonify({'message': "cookie not found!"}),401
        return f"Hello {user_id}"
        
            
    # @cross_origin(supports_credentials=True)
    @app.route("/login")
    def login():
        auth = True
        
        if not auth:
            return make_response("Could not verify",401,{"WWW-Authenticate" : 'Basic realm="Login required!"'})
        token = jwt.encode({'poblic_id':"12365","exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=2)},app.secret_key)
        # session['user'] = "current_user"
        session['user_id'] = token.decode('UTF-8')
        resp = make_response(jsonify({'token':token.decode('UTF-8')}))
        # resp.set_cookie('user_token', token.decode('UTF-8'), max_age=60)
        return resp

    return app