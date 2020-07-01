from flask import Flask, redirect,  url_for
from minnows import minnows
from fish import fish
from sharks import sharks

#app = Flask(__name__) --7/1/--test
app = Flask('blueprints_example2')
app.register_blueprint(minnows, url_prefix='/minnows')
app.register_blueprint(fish, url_prefix='/fish')
app.register_blueprint(sharks, url_prefix='/sharks')

@app.route("/")
def index():
   return redirect('/sharks')

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
