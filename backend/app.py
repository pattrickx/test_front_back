from flask import Flask, request, jsonify, make_response, session
from flask_cors import CORS
import jwt
import datetime
from functools import wraps
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = "101010" # ADD on .env key for DataBase

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': "token is missing!"}),401

        try: 
            data = jwt.decode(token,app.config['SECRET_KEY'])
            current_user = "current_user"
        except:
            return jsonify({'message': "token is invalid!"}),401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

def create_app(testing: bool = True):
    

    @app.route("/hello")
    @token_required
    def test(current_user):
        return f"HELLO token"

    @app.route("/user")
    def user():
        print(request.cookies)
        if not request.cookies.get('user_token'):
            return jsonify({'message': "cookie not found!"}),401
        return f"Hello {request.cookies.get('user_token')}"
        
            

    @app.route("/login")
    def login():
        auth = True
        
        if not auth:
            return make_response("Could not verify",401,{"WWW-Authenticate" : 'Basic realm="Login required!"'})
        token = jwt.encode({'poblic_id':"12365","exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=2)},app.config['SECRET_KEY'])
        # session['user'] = "current_user"
        resp = make_response(jsonify({'token':token.decode('UTF-8')}))
        resp.set_cookie('user_token', token.decode('UTF-8'), max_age=60,domain='https://back.knowcode.app/')
        return resp

    return app