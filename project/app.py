from flask import Flask, request, render_template, redirect, url_for
from functions import test_scale_generator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="GET":
#must remember it is always request.method==.... NOT just method==... and request needs importing
        return render_template('home.html')
    elif request.method=="POST":
        return redirect('/output') #or redirect(url_for("output"))



@app.route('/output', methods=["GET"])
def output():
    """
    return render_template('output.html')
"""
    return render_template(
        "output.html",
        title = "Your Scale",
        #username = user_login("beginner"),
        #new_scale = users_random_scale(user_login("beginner"), [])
        new_scale = str(test_scale_generator())
    )




if __name__ == '__main__':
   app.run(debug=True)
