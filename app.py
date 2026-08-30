from flask import Flask, request, jsonify, render_template
from frontend_blueprinting import frontend_bp
from config import Config
from exercise_api import ExerciseAPI
from db_utils_workouts import get_workouts_by_id, get_workouts_by_user_id, delete_workout, insert_workouts, update_workout
from routes.meal_routes import meal_bp

def create_app():
    # Create and configure the Flask aplication
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(frontend_bp)
    app.register_blueprint(meal_bp)

    # Home route confirms the API is running
    @app.get("/api/health")
    def health():
        # return a JSON response with application status
        return {
            "message": "GoalGetter is ready",
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
    @app.route("/workouts", methods=["GET", "POST"])
    @app.post("/workouts/create") #endpoint for creating workouts
    def workouts():

        if request.method == "GET":
            return {"message": "Workout API ready"}, 200 

        data = request.get_json()

        required_fields = ["user_id", "workout_date", "duration_minutes", "calories_burned"]

        if not data:
            return jsonify({"status":"error", "message":"A JSON object is required"}), 400
        
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
                return jsonify({"status": "error", 
                                "message": "Failed to create workout"}), 500
            
            return jsonify({
            "status": "success",
            "message": "Workout created successfully",
            "data": data
            }), 201
        
        except Exception:
            return jsonify({
            "status": "error",
            "message": "Failed to create workout",
            }), 500

    @app.route("/workouts/<workout_id>", methods=["GET"]) #endpoint for workout searched by workout id
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

    @app.get("/workouts/user/<user_id>")
    @app.get("/workouts/user/past_workouts/<user_id>") #endpoint for the users workouts
    def get_user_workouts(user_id):
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

        except Exception as e:
            return jsonify({
            "status": "error",
            "message": "Failed to retrieve workout",
            "error": str(e)
            }), 500
        
    @app.route("/workout/update/<workout_id>", methods=["PUT"]) #endpoint for updating workouts
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
            
            updated = update_workout(data, workout_id)

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

    @app.route("/workout/delete/<workout_id>", methods=['DELETE']) #endpoint for deleting a workout
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
    @app.get("/exercises")
    def exercises():
        equipment = request.args.get("equipment", "").strip() 
        body_part = request.args.get("body_part", "").strip() 
        exercise_type = request.args.get("exercise_type", "").strip() 
        name = request.args.get("name", "").strip()
        muscle = request.args.get("muscle", "").strip() 

        if not any([body_part, equipment, exercise_type, muscle, name]):
            return render_template(
                "workouts.html", 
                body_parts=BODY_PARTS,
                equipment=EQUIPMENT,
                categories=CATEGORIES,
                muscles=MUSCLES,
            )

        api = ExerciseAPI() 

        if equipment:
            results = api.search_by_equipment(equipment)
        elif body_part:
            results = api.search_by_body_part(body_part)
        elif exercise_type:
            results = api.search_by_exercise_type(exercise_type)
        elif name:
            results = api.search_by_name(name)
        else:
            results = api.search_by_target_muscle(muscle)

            # returning the html exercise card
        return render_template(
                "exercise_cards.html",
                exercises=results
            )
    
    # Equipment endpoint - getting all equipments 
    @app.route("/equipments")
    def equipments():
        api = ExerciseAPI() 
        try:
            results = api.get_all_equipments()
            return jsonify(results), 200 
        except Exception as e:
            return {"error": str(e)}, 500 
        
    #body part endpoint - getting all body parts  
    @app.route("/bodyparts")
    def bodyparts():
        api = ExerciseAPI() 
        try:
            results = api.get_all_body_parts()
            return jsonify(results), 200 
        except Exception as e:
            return {"error": str(e)}, 500 

    # exercise_type endpoint - getting all exercise types  
    @app.route("/exercisetypes")
    def exercisetypes():
        api = ExerciseAPI() 
        try:
            results = api.get_all_exercise_types()
            return jsonify(results), 200 
        except Exception as e:
            return {"error": str(e)}, 500 
        
    # target_muscles endpoint - getting all target muscles   
    @app.route("/targetmuscles")
    def targetmuscles():
        api = ExerciseAPI() 
        try:
            results = api.get_all_target_muscles()
            return jsonify(results), 200 
        except Exception as e:
            return {"error": str(e)}, 500 

    # Exercise detail route 
    @app.route("/exercises/<exercise_id>")
    def exercise_detail(exercise_id):

        api = ExerciseAPI() 

        try:
            exercise = api.get_exercise_details(exercise_id)
            return jsonify(exercise), 200 # success 
        
        except Exception as e:
            return {"error": str(e)}, 500 
        
    # workout-exercises endpoint
    @app.route("/workout-exercises")
    def workout_exercises():
        return {"message": "Workout Exercises endpoint ready"}, 200
    
    @app.route("/profile")
    def profile():
        return render_template("profile.html")
    
    @app.route("/login")
    def login ():
        return render_template("login.html")
    
    @app.route("/register")
    def register():
        return render_template("register.html")
    
    @app.route("/profile/edit")
    def edit_profile():
        return render_template("edit_profile.html")
    
    return app 
        

# create application instance 
app = create_app()

# run the application in debug mode 
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5001)