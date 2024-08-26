from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure random key

# In-memory storage
users = {}
community_posts = []
scenarios = [
    {"id": 1, "title": "Scenario 1", "description": "Description for scenario 1"},
    {"id": 2, "title": "Scenario 2", "description": "Description for scenario 2"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if email in users:
            flash('Email already registered. Please log in.', 'warning')
            return redirect(url_for('login'))

        # Hash the password and save the user in the dictionary
        hashed_password=generate_password_hash(password)
        users[email] = {'name': name, 'password': hashed_password}

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = users.get(email)

        if user and check_password_hash(user['password'], password):
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')

    return render_template('login.html')

@app.route('/scenarios')
def scenarios():
    return render_template('scenarios.html', scenarios=scenarios)

@app.route('/guidance')
def guidance():
    return render_template('guidance.html')

@app.route('/community', methods=['GET', 'POST'])
def community():
    if request.method == 'POST':
        post = request.form['post']
        community_posts.append(post)
        flash('Your post has been added!', 'success')

    return render_template('community.html', posts=community_posts)

if __name__ == '__main__':
    app.run(debug=True)
