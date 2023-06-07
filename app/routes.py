from app import app
from flask import render_template
#imports asdf.py  


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lub')
def lub():
    return "lubilubilubilub"

@app.route('/members')
def members():
    user = {'username': 'Shrek', 'shrexyness': '9000'}
    gmo = [
        { 
        'nick': 'lub',
        'desc': 'heisser splasher'
        },
        { 
        'nick': 'omat',
        'desc': 'weird dude'
        },{

        'nick': 'crissi',
        'desc': 'weird dude'
        },
        { 
        'nick': 'achoo',
        'desc': 'weird dude'
        },
        { 
        'nick': 'horkins',
        'desc': 'always mute'
        }
    ]
    return render_template('member.html',title='Home',user=user,gmo=gmo)



""" @app.route('/members/<string:name>')
def getMember(name):
    return render_template(
        'member.html',name=name)</string:name> """