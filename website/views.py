from flask import Blueprint,render_template, request,flash, current_app
from .words import words
from .config import *
from .models import UserInfo
from sqlalchemy.sql import text
from . import db
import datetime
import flask
initial_chance=10
views = Blueprint('views',__name__)
@views.route('/game', methods=['POST','GET'])

def game():
    if 'id' not in flask.session:
        return flask.redirect(flask.url_for('views.home'))
    print(flask.session)
    data = {"chance":initial_chance,"task":-1,"result":""}
    retrieve = UserInfo.query.filter_by(id=flask.session["id"]).first()
    data["task"]=retrieve.task
    data["chance"]=retrieve.chance
    data["status"]=data["task"]
    data["msg"]=""
    if request.method=='POST':
        
        if "purchase" in request.form:
            #smart contract call
            retrieve = UserInfo.query.filter_by(id=flask.session['id']).first()
            retrieve.chance =initial_chance
            retrieve.result = ""
            retrieve.task=request.form.get("purchase")
            db.session.add(retrieve)
            db.session.commit()
            data["task"]=retrieve.task
            data["chance"]=initial_chance
            data["status"]=retrieve.task
            # smart contract query
            return render_template("game.html",data=data)

        # user check correctness
        if 'ask' in request.form:
            query = request.form.get('ask')
            retrieve = UserInfo.query.filter_by(id=flask.session['id']).first()
            # no chance left
            if retrieve.chance==0:
                data["task"]=retrieve.task
                data["chance"]=retrieve.chance
                data["status"]=data["task"]
                return render_template("game.html",data=data)
            # use one chance
            retrieve.chance-=1
            db.session.add(retrieve)
            db.session.commit()

            # get user data
            data["task"]=retrieve.task
            data["chance"]=retrieve.chance
            data["status"]=data["task"]

            # check correctness of the answer
            for i in range(len(query)):
                if i>=len(words[data["task"]]):
                    break
                if query[i]==words[data["task"]][i]:
                    data["result"]+='*'
                else:
                    if query[i] in words[data["task"]]:
                        data["result"]+='o'
                    else:
                        data["result"]+='x'
            return render_template("game.html",data=data)
        # user submit answer
        if 'answer' in request.form:
            query = request.form.get('answer')

            for i in range(len(query)):
                if i>=len(words[data["task"]]):
                    break
                if query[i]==words[data["task"]][i]:
                    data["result"]+='*'
                else:
                    if query[i] in words[data["task"]]:
                        data["result"]+='o'
                    else:
                        data["result"]+='x'
            UserInfo.query.filter_by(id=flask.session['id']).first()
            if ('x' in data["result"] or 'o'in data["result"] or len(query)!=len(words[data["task"]])):
                data["win"]=-1
            else:
                data["win"]=1
            # update user data
            retrieve.task=-1
            retrieve.chance=initial_chance
            retrieve.result=""
            db.session.add(retrieve)
            db.session.commit()
            data["task"]=-1
            data["chance"]=initial_chance
            data["status"]=data["task"]

            # smart contract query
            return render_template("win.html",data=data)

    else:
        
        data["status"]=data["task"]
        return render_template("game.html",data=data)


@views.route('/', methods=['POST','GET'])
def home():
    if request.method=='POST':
        id = request.headers.get("Content-Type")
        exists = UserInfo.query.filter_by(id=id).first() is not None
        if not exists:
            chance=initial_chance
            task=-1
            userinfo = UserInfo(id=id,chance=chance,task=task)
            db.session.add(userinfo)
            db.session.commit()
        flask.session["id"]=id;
        flask.session["time"]=datetime.datetime.now().timestamp();
    return render_template("connect.html")
