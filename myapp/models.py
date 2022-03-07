from myapp import db
from datetime import datetime


class UserData(db.Model):
    __tablename__ = "userdata"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)
    amid = db.Column(db.String(64))

    def __init__(self, name, amid):
        self.name = name
        self.amid = amid

    def __repr__(self):
        return f"<User {self.name}>"


class TalkData(db.Model):
    __tablename__ = "talkdata"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    body = db.Column(db.Text)
    create_timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, body):
        self.name = name
        self.body = body
        self.create_timestamp = datetime.utcnow()

    def __repr__(self):
        return f"<Talk {self.id}>"

    def create(self):
        db.session.add(self)
        db.session.commit()
        return repr(self)

    @staticmethod
    def read_all():
        return TalkData.query.all()

    def remove(self):
        db.session.delete(self)
        db.session.commit()
        return "Data be Remove"
