from flask import Flask, render_template  # import Flask, and render_template
from data import Users # users data

# placeholder for the current module (app.py)
app = Flask(__name__)

# app routes
# root
@app.route('/')
def index():
    return render_template('index.html') # return index template
# executed app
if __name__ == '__main__':
    app.run(debug=True) # debug=True updates View if detects changes
