from flask import Flask
from flask import render_template 

app = Flask(__name__)

# Routes to Render Something

@app.route('/about')
def about():
    return render_template('about.html')


    





