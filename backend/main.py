from flask import request, jsonify
from config import app, db
from models import Goal


@app.route("/")
def hello():
    return "<h1>Hello World</h1>"


@app.route("/goals", methods=["GET"])
def get_goals():
    goals = Goal.query.all()
    json_goals = list(map(lambda x: x.to_json(), goals))
    return jsonify({"goals": json_goals})

@app.route("/create_goal", methods=["POST"])
def create_goal():
    name = request.json.get("name")
    desc = request.json.get("desc")
    color = request.json.get("color")

    if not name:
        return(
            jsonify({"message": "You must include a name"})
        )
    
    new_goal = Goal(goal_name=name, goal_desc=desc, goal_color=color)
    try: 
        db.session.add(new_goal)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "Goal Created"}), 201

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)