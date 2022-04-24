from flask import flash, Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from App.models import db,Word
from gtts import gTTS
import os



from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    get_all_words_json,
    authenticate,
    start_game,
    check_word,
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')


@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/api/users')
def client_app():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/lol')
def lol():
    return 'lol'

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')

@user_views.route('/signup' ,methods=['POST' , 'GET'])
def signup():
    if request.method == 'POST':
        data = request.form
        create_user(data['username'], data['password'])
        try:
            
            return render_template('landing.html')
        except:
            print('error')
            return render_template('index.html')

@user_views.route('/login_form', methods=['GET', 'POST'])
def login_form():
    
    if request.method == 'POST':
        data=request.form
        if data['username_login'] != 'bob' and data['username_login'] != 'bobpass' :
            print ("error")
        else:
            return render_template('landing.html')
    return render_template('login.html')
    


@user_views.route('/signup_re', methods=['POST', 'GET'])
def redirect():
    return render_template('index.html')

@user_views.route('/play', methods=['POST', 'GET'])
def play():
    return render_template('landing.html')

@user_views.route('/login' ,methods=['POST', 'GET'])
def login():
    return render_template('login.html')

@user_views.route('/words', methods = ['GET', 'POST'])
def test():
    words = start_game(1)
    data= request.form
     

    #words = Word.query.all()
    if request.method == 'POST':
        
        
        if data['dis'] == data['word_guess']:
            
            flash("Correct")
            
            return render_template('landing.html', words = words)
        else:
            flash("Dam bro youre so wrong lmao")

    return render_template('landing.html', words = words)

