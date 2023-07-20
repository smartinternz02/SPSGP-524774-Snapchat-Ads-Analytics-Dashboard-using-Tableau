from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/function1')
def function1():
    # Replace this with your desired function logic for Function 1
    return render_template('Tableu.html')

@app.route('/function2')
def function2():
    # Replace this with your desired function logic for Function 2
    return render_template('Tableu2.html')

if __name__ == '__main__':
    app.run()
