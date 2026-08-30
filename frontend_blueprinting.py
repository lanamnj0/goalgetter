"""
    Blueprint Refactoring – Work in Progress

    This file demonstrates the implementation of Flask Blueprints to organise frontend routes.
    The blueprint is registered in app.py, and all frontend templates are served through it.

    Integration of teammates' backend functions is planned.
    Currently, mock data is used for frontend testing and demonstration.
    This follows industry-standard Flask architecture patterns.

NOTE:
    Inside the @frontend_bp.route(</route_name>) must be an identical match to the <href="/..."> in the layout.html file for the UI to correspond to the backend.

"""

import time
from flask import Blueprint, Flask, flash, redirect, render_template, request, url_for

SAMPLE_WORKOUTS = [
    {
        "date": "2026-06-18",
        "exercise": "Arm Day",
        "duration": 35,
        "calories": 240,
    },
    {
        "date": "2026-06-20",
        "exercise": "Upper Body",
        "duration": 40,
        "calories": 280,
    },
    {
        "date": "2026-06-22",
        "exercise": "Leg Day",
        "duration": 45,
        "calories": 320,
    },
]

# 'frontend' is the internal name, __name__ helps Flask locate templates
frontend_bp = Blueprint('frontend', __name__)

# This is the dashboard homepage
@frontend_bp.route('/')
def index():
    # Here is the calendar and widgets on the dashboard
    return render_template('dashboard.html')

@frontend_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@frontend_bp.route('/meals_and_recipes')
def meals_and_recipes():
    # Hardcoded mock data – like an API response
    meals = [
        {
            'id': 1,
            'name': 'Greek Salad',
            'description': 'Fresh vegetables, feta cheese, olives, and a light dressing.',
            'image_url': '../static/greek-salad-test-image.jpeg',  # placeholder images
            'prep_time': 15,
            'calories': 320
        },
        {
            'id': 2,
            'name': 'Grilled Chicken',
            'description': 'Herb-marinated chicken breast with roasted vegetables.',
            'image_url': '../static/grilled-chicken-test-image.jpeg',
            'prep_time': 25,
            'calories': 420
        },
        {
            'id': 3,
            'name': 'Protein Smoothie',
            'description': 'Banana, berries, whey protein, and almond milk.',
            'image_url': '../static/protein-smoothie-test-image.jpeg',
            'prep_time': 5,
            'calories': 250
        },
        # Some examples, more could be added.
    ]
    return render_template('meals_and_recipes.html', meals=meals)

@frontend_bp.route('/history')
def history():
    return render_template(
        'history.html',
        workouts=reversed(SAMPLE_WORKOUTS),
        )

@frontend_bp.route('/support', methods=['GET', 'POST'])
def support():
    if request.method == 'POST':
        # Grabs all data from form
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        selected_issue = request.form.get('support_category')

        # Mock validation to check required fields exist
        if name and email and message and selected_issue:
            # Generating a fake ticket number using time module, unique number every second
            fake_ticket_number = int(time.time()) # Do not want a float

            # flash() sucessful message with the fake ticket number
            flash(f"Thank you {name}! Your support ticket #{fake_ticket_number} has been submitted! A team member will email your shortly", "success")

        else: # If some or any of the fields are missing from the form
            flash("Please fill out all the required fields before submitting", "info")

    return render_template('support.html')

@frontend_bp.get('/settings')
def settings():
    return render_template('settings.html')

@frontend_bp.route('/logout')
def logout():
    return render_template('logout.html')
