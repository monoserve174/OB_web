from flask import render_template, flash, redirect, url_for, request
from myapp import app, db
from myapp.models import UserData, TalkData


@app.shell_context_processor
def shellContext():
    return dict(db=db,
                UserData=UserData,
                TalkData=TalkData,)


# 首頁
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# 報名頁
@app.route('/join', methods=["GET", "POST"])
def join():
    if request.method == "POST":
        formName = request.form.get("formName")
        if formName == "joinForm":
            userId = request.form.get("userId")
            if userId:
                user = UserData.query.filter_by(id=userId).first()
                user.name = request.form.get("userName")
                user.amid = request.form.get("userAmid")
                db.session.add(user)
                try:
                    db.session.commit()
                    flash(f"修改成功")
                    return redirect(url_for('joinerinfo'))
                except Exception as e:
                    print(f"修改失敗: {e}")
                    flash("修改失敗")
                    db.session.rollback()
            else:
                userName = request.form.get("userName")
                userAmid = request.form.get("userAmid")
                user = UserData(userName, userAmid)
                db.session.add(user)
                try:
                    db.session.commit()
                    flash(f"參加成功")
                    return redirect(url_for('joinerinfo'))
                except Exception as e:
                    print(f"參加失敗: {e}")
                    flash("參加失敗")
                    db.session.rollback()
        elif formName == "editUser":
            userId = request.form.get("userId")
            user = UserData.query.filter_by(id=userId).first()
            return render_template('join.html', user=user)
        elif formName == "delUserForm":
            userId = request.form.get("userId")
            user = UserData.query.filter_by(id=userId).first()
            db.session.delete(user)
            try:
                db.session.commit()
                flash(f"刪除成功。")
                return redirect(url_for('joinerinfo'))
            except Exception as e:
                print(f"刪除失敗: {e}")
                flash("刪除失敗")
                db.session.rollback()
    return render_template('join.html')


# @app.route('/editteam', methods=["GET", "POST"])
# def editteam():
#     if request.method == "POST":
#         teamsid = request.form.get('teamid')
#         if request.form.get("formName"):
#             teamName = request.form.get('teamName')
#             teamPlayer = request.form.get('teamPlayer')
#             team = TeamData.query.filter_by(sid=teamsid).first()
#             team.name = teamName
#             team.player = teamPlayer
#             db.session.add(team)
#             flash(f"隊伍資料修改完成。")
#             db.session.commit()
#         else:
#             # 讀取資料
#             team = TeamData.query.filter_by(sid=teamsid).first()
#             if team:
#                 return render_template('join.html', team=team)
#             else:
#                 flash("驗證碼錯誤，請確認後再次輸入")
#                 return redirect(url_for('teaminfo'))


@app.route('/joinerinfo')
def joinerinfo():
    userData = UserData.query.all()
    return render_template('joinerinfo.html', userData=userData)


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/playtime')
def playtime():
    # return render_template('playtime.html')
    return redirect(url_for('bulid'))


@app.route('/messages')
def messages():
    messages = TalkData.query.all()[::-1]
    return render_template('message.html', messages=messages)


@app.route('/addMessage', methods=['POST'])
def addmessage():
    messageName = request.form.get("messageName")
    messageBody = request.form.get("messageBody")
    TalkData(messageName, messageBody).create()
    return redirect(url_for('messages'))


@app.route('/removeMessage', methods=['POST'])
def removemessage():
    messageId = int(request.form.get("messageId"))
    TalkData.query.get(messageId).remove()
    flash("刪除成功")
    return redirect(url_for('messages'))


@app.route('/bulid')
def bulid():
    return render_template('bulid.html')

