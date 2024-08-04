from config import db

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal_name = db.Column(db.String(80), unique=True, nullable=False)
    goal_desc = db.Column(db.String(280), nullable=True)
    goal_color = db.Column(db.String(7), default="#F0F3F5")
    
    milestones = db.relationship("Milestone", backref="goal")

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "desc": self.desc,
            "color": self.color
        }

class Milestone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    milestone_name = db.Column(db.String(80), unique=True, nullable=False)
    milestone_desc = db.Column(db.String(280), nullable=True)
    milestone_color = db.Column(db.String(7), default="#F0F3F5")

    goal_id = db.Column(db.Integer, db.ForeignKey("goal.id"))

    achievements = db.relationship("Achievements", backref="milestone")

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "desc": self.desc,
            "color": self.color
        }

class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    achievement_name = db.Column(db.String(80), unique=True, nullable=False)
    achievement_desc = db.Column(db.String(280), nullable=True)
    achievement_color = db.Column(db.String(7), default="#F0F3F5")

    milestone_id = db.Column(db.Integer, db.ForeignKey("milestone.id"))

    tasks = db.relationship("Tasks", backref="achievement")

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "desc": self.desc,
            "color": self.color
        }

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(80), unique=True, nullable=False)
    task_desc = db.Column(db.String(280), nullable=True)
    task_color = db.Column(db.String(7), default="#F0F3F5")
    
    achievement_id = db.Column(db.Integer, db.ForeignKey("achievement.id"))

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "desc": self.desc,
            "color": self.color
        }
