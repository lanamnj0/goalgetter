from flask import Flask, render_template

app = Flask(__name__)

# This is the dashboard homepage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/workouts')
def workouts():
    return render_template('workouts.html')

@app.route('/meals_and_recipes')
def meals_and_recipes():
    return render_template('meals_and_recipes.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True)

# To run file: python frontend.py