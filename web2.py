from flask import Flask, render_template, session, redirect, url_for, make_response
from flask import request
import random


app = Flask(__name__)

# make matrix of strings and append to it str(int) str(double) str(char) str(date)
# then we can simple rotate it to produce the file
def int_generator(num_rows):
    for x in range(int(num_rows)):
        num = random.randint(-2**31,2**31)
        session["csv"] = [[0 for x in range(4)] for y in range(int(num_rows))] 
        session["csv"][0][x] = num


@app.route('/', methods = ['GET','POST'])
def file_setup():
    if request.method == "POST":
        print "HEREEEEE"
        method_1 = request.form.getlist("myInputs[]")
        num_rows = request.form["num_rows"] #number of rows
        print str(request.form.getlist("myInputs[]"))
        print "JIHIHI"
        if method_1 == "Int":
            print request.form["myInputs[]"]
            return "HI"
            #int_generator(num_rows)
            #return redirect (url_for("file_out"))

    return render_template("home.html") #html for page




@app.route('/file_out')
def file_out():
    # We need to modify the response, so the first thing we
    # need to do is create a response out of the CSV string
    csv = (session["csv"])
    response = make_response(csv)
    # This is the key: Set the right header for the response
    # to be downloaded, instead of just printed on the browser
    response.headers["Content-Disposition"] = "attachment; filename=response.txt"
    return response



if __name__ == '__main__':
    app.secret_key = 'secretkeyhere'
    app.run(debug = 'True')




