from flask import Flask, jsonify, request
from config import Config
from db_utils import get_workouts_by_id, get_workouts_by_user_id, delete_workout, insert_workouts, update_workout

def create_app():
    # Create and configure the Flask aplication
    app = Flask(__name__)
    app.config.from_object(Config)

    # Home route confirms the API is running
    @app.route("/")
    def home():
        # return a JSON response with application status
        return {
            "message": "Welcome to GoalGetter - Track workouts, meals and fitness goals",
            "status": "running"
        }, 200

    # Users endpoint
    @app.route("/users")
    def users():
        # return a JSON response
        return {"message": "Users endpoint ready"}, 200

    # Meals endpoint
    @app.route("/meals")
    def meals():
        return {"message": "Meals endpoint ready"}, 200

    # Goals endpoint
    @app.route("/goals")
    def goals():
        return {"message": "Goals endpoint ready"}, 200

    # Workouts endpoint
    @app.route("/workouts")
    def workouts():
        return {"message": "Workouts endpoint ready"}, 200
    
    @app.route("/workouts", methods=["POST"])
    def create_workout():

        data = request.get_json()

        required_fields = ["user_id", "workout_date", "duration_minutes", "calories_burned"]

        if not data:
            return jsonify({"status":"error", "message":"There's no JSON data received"}), 400
        
        for field in required_fields:
            if field not in data:
                return jsonify({
                "status": "error",
                "message": f"Missing field: {field}"
            }), 400

        try:
            insert_data = (
                data["user_id"], data["workout_date"], data["duration_minutes"], data["calories_burned"]
                )
            
            new_workout = insert_workouts("workouts", insert_data)

            if not new_workout:
                return jsonify({"status": "error", "message": "Failed to create workout"}), 500
            
            return jsonify({
            "status": "success",
            "message": "Workout created successfully",
            "data": data
            }), 201
        except Exception as e:
            return jsonify({
            "status": "error",
            "message": "Failed to create workout",
            "error": str(e)
            }), 500

    @app.route("/workouts/<workout_id>", methods=["GET"])
    def get_workout_id_api(workout_id):
        try:
            workout_id = int(workout_id)
        except ValueError:
            return jsonify({"status": "Error", "message": "Invalid workout ID"}), 400
        try: 
            workout = get_workouts_by_id(workout_id)
            
            if not workout:
                return jsonify({"status": "error", "message": "Workout not found"}), 404
            
            return jsonify({"status": "Workout found", "data": workout}), 200
        
        except Exception as e:
                return jsonify({
                "status": "error",
                "message": "Failed to retrieve workout",
                "error": str(e)
                }), 500
        
    @app.route("/workouts/user/<user_id>", methods=["GET"])
    def get_workout_user_api(user_id):
        try:
            user_id = int(user_id)
        except ValueError:
            return jsonify({"status": "Error", "message": "Invalid user ID"}), 400
        try: 
            workout = get_workouts_by_user_id(user_id)
            
            if not workout:
                return jsonify({"status": "error", "message": "Workout not found"}), 404
            
            return jsonify({"status": "Workout found", "data": workout}), 200
        
        except Exception as e:
                return jsonify({
                "status": "error",
                "message": "Failed to retrieve workout",
                "error": str(e)
                }), 500
        
    @app.route("/workout/update/<workout_id>", method=["PUT"])
    def update_workout_api(workout_id):
        try:
            workout_id = int(workout_id)
        except ValueError:
            return jsonify({"status": "Error", "message": "Invalid workout ID"}), 400

        data = request.get_json()

        if not data:
            return jsonify({"status":"error", "message":"There's no JSON data received"}), 400
        try:
            existing = get_workouts_by_id(workout_id)
            if not existing:
                return jsonify({"status": "error", "message": "Workout not found"}), 404
            
            updated = update_workout(workout_id, data)

            if not updated:
                return jsonify({"status": "error", "message": "No fields to update"}), 400
            
            return jsonify({
            "status": "success",
            "message": "Workout updated successfully",
            "data": data
            }), 200
        except Exception as e:
                return jsonify({
                "status": "error",
                "message": "Failed to update workout",
                "error": str(e)
                }), 500

    @app.route("/workout/delete/<workout_id>", methods=['DELETE'])
    def delete_workout_api(workout_id):
        try:
            workout_id = int(workout_id)
        except ValueError:
            return jsonify({"status": "Error", "message": "Invalid workout ID"}), 400
        
        try:
            workout = get_workouts_by_id(workout_id)
            if not workout:
                return jsonify({"status": "error", "message": "Workout not found"}), 404
            
            delete_workout(workout_id)
            
            return jsonify({"status": "Workout has been deleted", "data": workout}), 200
        
        except Exception as e:
                return jsonify({
                "status": "error",
                "message": "Failed to delete workout",
                "error": str(e)
                }), 500


    # exercises endpoint
    @app.route("/exercises")
    def exercises():
        return {"message": "Exercises endpoint ready"}, 200

    # workout-exercises endpoint
    @app.route("/workout-exercises")
    def workout_exercises():
        return {"message": "Workout Exercises endpoint ready"}, 200

    return app

# create application instance 
app = create_app()

# run the application in debug mode 
if __name__ == "__main__":
    app.run(debug=True)
