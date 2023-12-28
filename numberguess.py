from flask import Flask, render_template, request
import random
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Move secret_number generation outside the home function
secret_number = None

@app.route('/', methods=['GET', 'POST'])
def home():
    global secret_number  # Use the global keyword to access the outer variable

    if request.method == 'POST':
        if secret_number is None:
            secret_number = generate_secret_number()

        user_guess = int(request.form['user_guess'])
        result_message, reset_game = check_guess(user_guess, secret_number)

        if reset_game:
            secret_number = generate_secret_number()

        return render_template('index.html', result_message=result_message)

    return render_template('index.html', result_message=None)

def generate_secret_number():
    return random.randint(0, 100)

def check_guess(user_guess, secret_number):
    if user_guess == secret_number:
        return 'Congratulations! You guessed the correct number.', True
    elif user_guess < secret_number:
        return 'Too low! Try again.', False
    else:
        return 'Too high! Try again.', False

if __name__ == '__main__':
    app.run(debug=True)
