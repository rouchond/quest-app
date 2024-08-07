from flask import request, jsonify
from config import app, db
from models import Goal, Milestone, Achievement, Task


@app.route("/")
def hello():
    return "<h1>Hello World</h1>"

#####
##### Goal Routes
#####

@app.route("/goals", methods=["GET"])
def get_goals():
    goals = Goal.query.all()
    json_goals = list(map(lambda x: x.to_json(), goals))
    return jsonify({"goals": json_goals})

@app.route("/goals/<int:goal_id>", methods=["GET"])
def get_goal(goal_id):
    goal = db.session.get(Goal, goal_id)
    if not goal:
        return jsonify({"message": "Goal not found."}), 404
    return jsonify({"goal": goal.to_json()})

@app.route("/create_goal", methods=["POST"])
def create_goal():
    name = request.json.get("name")
    desc = request.json.get("desc")
    color = request.json.get("color")

    if not name:
        return(
            jsonify({"message": "You must include a name"}), 400
        )
    
    new_goal = Goal(goal_name=name, goal_desc=desc, goal_color=color)
    try: 
        db.session.add(new_goal)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "Goal Created"}), 201

@app.route("/update_goal/<int:goal_id>", methods=["PUT"])
def update_goal(goal_id):
    goal = db.session.get(Goal, goal_id)
    if not goal:
        return jsonify({"message": "Goal not found"}), 404
    
    data = request.json

    goal.goal_name  = data.get("name", goal.goal_name)
    goal.goal_desc  = data.get("desc", goal.goal_desc)
    goal.goal_color  = data.get("color", goal.goal_color)

    db.session.commit()

    return jsonify({"message": "Goal updated"}), 200

@app.route("/delete_goal/<int:goal_id>", methods=["DELETE"])
def delete_goal(goal_id):
    goal = db.session.get(Goal, goal_id)
    if not goal:
        return jsonify({"message": "Goal not found."}), 404
    
    db.session.delete(goal)
    db.session.commit()

    return jsonify({"message": "Goal deleted."}), 200

#####
##### Milestone Routes
#####

@app.route("/milestones", methods=["GET"])
def get_milestones():
    milestones = Milestone.query.all()
    json_milestones = list(map(lambda x: x.to_json(), milestones))
    return jsonify({"milestones": json_milestones})

@app.route("/milestones/<int:milestone_id>", methods=["GET"])
def get_milestone(milestone_id):
    milestone = db.session.get(Milestone, milestone_id)
    if not milestone:
        return jsonify({"message": "Milestone not found"}), 404
    
    return jsonify({"milestone": milestone.to_json()})

@app.route("/create_milestone", methods=["POST"])
def create_milestone():
    name = request.json.get("name")
    desc = request.json.get("desc")
    color = request.json.get("color")

    if not name:
        return jsonify({"message": "You must include a name"}), 400
    
    new_milestone = Milestone(milestone_name=name, milestone_desc=desc, milestone_color=color)
    try:
        db.session.add(new_milestone)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "Milestone Created"}), 201


@app.route("/update_milestone/<int:milestone_id>", methods=["PUT"])
def update_milestone(milestone_id):
    milestone = db.session.get(Milestone, milestone_id)
    if not milestone:
        return jsonify({"milestone": "Milestone not found"}), 404
    
    data = request.json

    milestone.milestone_name = data.get("name", milestone.milestone_name)
    milestone.milestone_desc = data.get("desc", milestone.milestone_desc)
    milestone.milestone_color = data.get("color", milestone.milestone_color)

    db.session.commit()
    return jsonify({"message": "Updated Milestone"})


@app.route("/delete_milestone/<int:milestone_id>", methods=["DELETE"])
def delete_milestone(milestone_id):
    milestone = db.session.get(Milestone, milestone_id)
    if not milestone:
        return jsonify({"message": "Milestone not found"}), 404
    
    db.session.delete(milestone)
    db.session.commit()
    return jsonify({"message": "Milestone deleted"})

#####
##### Achievement Routes
#####

@app.route("/achievements", methods=["GET"])
def get_achievements():
    achievement = Achievement.query.all()
    json_achievements = list(map(lambda x: x.to_json(), achievement))
    return jsonify({"achievements": json_achievements})

@app.route("/achievements/<int:achievement_id>", methods=["GET"])
def get_achievement(achievement_id):
    achievement = db.session.get(Achievement, achievement_id)
    if not achievement:
        return jsonify({"message": "Achievement not found"}), 404
    
    return jsonify({"milestone": achievement.to_json()})

@app.route("/create_achievement", methods=["POST"])
def create_achievement():
    name = request.json.get("name")
    desc = request.json.get("desc")
    color = request.json.get("color")

    if not name:
        return jsonify({"message": "You must include a name"}), 400
    
    new_achievement = Achievement(achievement_name=name, achievement_desc=desc, achievement_color=color)
    try:
        db.session.add(new_achievement)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "Achievement Created"}), 201


@app.route("/update_achievement/<int:achievement_id>", methods=["PUT"])
def update_achievement(achievement_id):
    achievement = db.session.get(Achievement, achievement_id)
    if not achievement:
        return jsonify({"achievement": "Achievement not found"}), 404
    
    data = request.json

    achievement.achievement_name = data.get("name", achievement.achievement_name)
    achievement.achievement_desc = data.get("desc", achievement.achievement_desc)
    achievement.achievement_color = data.get("color", achievement.achievement_color)

    db.session.commit()
    return jsonify({"message": "Updated Achievement"})


@app.route("/delete_achievement/<int:achievement_id>", methods=["DELETE"])
def delete_achievement(achievement_id):
    achievement = db.session.get(Achievement, achievement_id)
    if not achievement:
        return jsonify({"message": "Achievement not found"}), 404
    
    db.session.delete(achievement)
    db.session.commit()
    return jsonify({"message": "Achievement deleted"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)