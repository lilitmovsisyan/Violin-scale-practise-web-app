from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="GET":
#must remember it is always request.method==.... NOT just method==... and request needs importing
        return render_template('home.html')
    elif request.method=="POST":
        return redirect('/output') #or redirect(url_for("output"))



@app.route('/output')
def output():
    render_template('output.html')
"""
    return render_template(
        "output.html",
        title="Generator",
        new_scale=new_scale,
    )
"""



if __name__ == '__main__':
   app.run(debug=True)
