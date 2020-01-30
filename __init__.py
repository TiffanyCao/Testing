#Tiffany Cao
#SoftDev1 pd1
#K
#2019

from flask import Flask, render_template
import os
app = Flask(__name__)

DIR = os.path.dirname(__file__)
DIR += '/'

@app.route('/')
def hello_world():
    print("hello")
    return "hello world"

coll = [0, 1, 1, 2, 3, 5, 8]

@app.route("/my_foist_template")
def test_tmplt():
    return render_template('tmplt.html',
                            foo = "foooo",
                            collection = coll)

if __name__ == "__main__":
    app.debug = True
    app.run()
