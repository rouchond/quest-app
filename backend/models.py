from config import db

class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quest_name = db.Column(db.String(80), unique=True, nullable=False)
    quest_data = db.Column(db.String(280), unique=False, nullable=True)


class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    achievement_name = db.Column(db.String(80), unique=True, nullable=False)
    achievement_data = db.Column(db.String(280), unique=False, nullable=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(80), unique=True, nullable=False)
    task_data = db.Column(db.String(280), unique=False, nullable=True)
    
