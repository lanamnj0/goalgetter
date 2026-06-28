from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.meal import suggest_meal_plan, calculate_total_nutrition, generate_weekly_meal_variations


meal_bp = Blueprint("meals", __name__, url_prefix="/meal-plans")

meal_plans = []


@meal_bp.route("/", methods=["GET"])
def view_meal_plans():
    meals = [
        {
            "id": 1,
            "name": "Greek Power Salad",
            "description": "Fresh Vegetables, Feta, Olives and a Light Lemon Dressing.",
            "image_url": "/static/images/greekpowersalad.png",
            "prep_time": 15,
            "calories": 320,
            "goal": "Weight Loss"
        },
        {
            "id": 2,
            "name": "Chicken Couscous Bowl",
            "description": "Lean Chicken Breast With Hoisin Sauce, Couscous, Vegetables and a High Protein Balance.",
            "image_url": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=900&q=80",
            "prep_time": 25,
            "calories": 720,
            "goal": "Muscle Gain"
        },
        {
            "id": 3,
            "name": "Protein Oats",
            "description": "Oats, Banana and Protein Powder for a Filling Breakfast.",
            "image_url": "/static/images/bananaoats.jpg",
            "prep_time": 10,
            "calories": 650,
            "goal": "Muscle Gain"
        },
        {
            "id": 4,
            "name": "Salmon Veg Plate",
            "description": "Grilled Salmon with Mixed Vegetables for a Balanced Meal.",
            "image_url": "https://images.unsplash.com/photo-1712334562767-5d366d0c40d9?q=80&w=735&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "prep_time": 30,
            "calories": 520,
            "goal": "Weight Loss"
        },
        {
            "id": 5,
            "name": "Berry Yoghurt Bowl",
            "description": "Greek Yoghurt, Berries and Chia Seeds for a Light Snack.",
            "image_url": "/static/images/berryyoghurtbowl.png",
            "prep_time": 8,
            "calories": 330,
            "goal": "Weight Loss"
        },
        {
            "id": 6,
            "name": "Turkey Pasta",
            "description": "Turkey Mince Pasta with Tomato Sauce for Energy and Protein.",
            "image_url": "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?auto=format&fit=crop&w=900&q=80",
            "prep_time": 35,
            "calories": 760,
            "goal": "Muscle Gain"
        },
        {
            "id": 7,
            "name": "Naked Chicken Burrito Bowl",
            "description": "Grilled Chicken, Rice, Black Beans, Sweetcorn, Avocado, Lettuce and Salsa in a Fresh Burrito Bowl.",
            "image_url": "/static/images/naked_chicken_burrito_bowl.png",
            "prep_time": 25,
            "calories": 610,
            "goal": "Muscle Gain"
        },
        {
            "id": 8,
            "name": "Steak Rice Bowl",
            "description": "Tender Steak Strips Served With Rice, Peppers, Greens and a Light Garlic Dressing.",
            "image_url": "/static/images/steak_rice_bowl.png",
            "prep_time": 30,
            "calories": 690,
            "goal": "Muscle Gain"
        },
        {
            "id": 9,
            "name": "Avocado Egg Toast",
            "description": "Toasted sourdough topped with smashed avocado, boiled eggs, chilli flakes and fresh herbs.",
            "image_url": "https://images.unsplash.com/photo-1525351484163-7529414344d8?q=80&w=880&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "prep_time": 12,
            "calories": 410,
            "goal": "Weight Loss"
        },
        {
            "id": 10,
            "name": "Loaded Sweet Potato",
            "description": "Baked Sweet Potato Topped with Beef, Black Beans, Avocado, Salsa and a layer of Cream Cheese.",
            "image_url": "/static/images/loaded_sweet_potato.png",
            "prep_time": 35,
            "calories": 520,
            "goal": "Weight Loss"
        },
        {
            "id": 11,
            "name": "Prawn Mango Quinoa Bowl",
            "description": "Juicy Prawns, Quinoa, Mango, Cucumber, Avocado and Lime Dressing for a Fresh Tropical Bowl.",
            "image_url": "https://www.dishbydish.net/wp-content/uploads/2013/07/quinoa-salad-2-blog.jpg",
            "prep_time": 22,
            "calories": 490,
            "goal": "Weight Loss"
        },
        {
            "id": 12,
            "name": "Falafel Hummus Plate",
            "description": "Crispy Falafel Served with Hummus, Cucumber, Tomatoes, Flatbread and a Lemon Herb Salad.",
            "image_url": "https://beingnutritious.com/wp-content/uploads/2022/07/Baked-falafel-wrap-scaled.jpg",
            "prep_time": 20,
            "calories": 560,
            "goal": "Weight Loss"
        }
    ]

    return render_template("meals/list.html", meals=meals)


@meal_bp.route("/create", methods=["GET", "POST"])
def create_meal_plan():
    if request.method == "POST":
        title = request.form.get("title")
        goal = request.form.get("goal")

        if not title or not goal:
            flash("Please enter a title and select a goal.", "danger")
            return redirect(url_for("meals.create_meal_plan"))

        meal_plan = suggest_meal_plan(goal)
        meal_plan.title = title

        meal_plans.append(meal_plan)
        plan_id = len(meal_plans) - 1

        flash("Meal plan created successfully.", "success")
        return redirect(url_for("meals.view_single_meal_plan", plan_id=plan_id))

    return render_template("meals/create.html")


@meal_bp.route("/<int:plan_id>", methods=["GET"])
def view_single_meal_plan(plan_id):
    if plan_id < 0 or plan_id >= len(meal_plans):
        flash("Meal plan not found.", "danger")
        return redirect(url_for("meals.view_meal_plans"))

    meal_plan = meal_plans[plan_id]
    totals = calculate_total_nutrition(meal_plan)

    return render_template(
        "meals/detail.html",
        meal_plan=meal_plan,
        totals=totals,
        plan_id=plan_id
    )


@meal_bp.route("/<int:plan_id>/weekly", methods=["GET"])
def weekly_created_meal_plan(plan_id):
    if plan_id < 0 or plan_id >= len(meal_plans):
        flash("Meal plan not found.", "danger")
        return redirect(url_for("meals.view_meal_plans"))

    base_plan = meal_plans[plan_id]
    weekly_plans = generate_weekly_meal_variations(base_plan, total_days=7)

    return render_template(
        "meals/weekly.html",
        weekly_plans=weekly_plans,
        goal=base_plan.goal,
        plan_id=plan_id
    )


@meal_bp.route("/<int:plan_id>/update", methods=["GET", "POST"])
def update_meal_plan(plan_id):
    if plan_id < 0 or plan_id >= len(meal_plans):
        flash("Meal plan not found.", "danger")
        return redirect(url_for("meals.view_meal_plans"))

    meal_plan = meal_plans[plan_id]

    if request.method == "POST":
        title = request.form.get("title")
        goal = request.form.get("goal")

        if not title or not goal:
            flash("Please enter a title and select a goal.", "danger")
            return redirect(url_for("meals.update_meal_plan", plan_id=plan_id))

        updated_plan = suggest_meal_plan(goal)
        updated_plan.title = title

        meal_plans[plan_id] = updated_plan

        flash("Meal plan updated successfully.", "success")
        return redirect(url_for("meals.view_single_meal_plan", plan_id=plan_id))

    return render_template(
        "meals/update.html",
        meal_plan=meal_plan,
        plan_id=plan_id
    )


@meal_bp.route("/<int:plan_id>/delete", methods=["POST"])
def delete_meal_plan(plan_id):
    if plan_id < 0 or plan_id >= len(meal_plans):
        flash("Meal plan not found.", "danger")
        return redirect(url_for("meals.view_meal_plans"))

    meal_plans.pop(plan_id)

    flash("Meal plan deleted successfully.", "success")
    return redirect(url_for("meals.view_meal_plans"))


@meal_bp.route("/suggest/<goal>", methods=["GET"])
def suggested_meal_plan(goal):
    meal_plan = suggest_meal_plan(goal)
    totals = calculate_total_nutrition(meal_plan)

    return render_template(
        "meals/detail.html",
        meal_plan=meal_plan,
        totals=totals,
        plan_id=None
    )