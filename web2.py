from flask import Flask, render_template, session, redirect, url_for, make_response
from flask import request
import random


app = Flask(__name__)

# make matrix of strings and append to it str(int) str(double) str(char) str(date)
# then we can simple rotate it to produce the file
def rand_str(length):
    alphanum = 'abcdefghijklmnopqrstuvwxyz0123456789'
    id = ''
    for i in range(length):
        id += random.choice(alphanum)
    return id

def int_generator(num_rows,col_num):
    session[col_num] = ""
    for x in range(int(num_rows)):
        num = random.randint(-2**31,2**31)
        #session["csv"] = [[0 for x in range(4)] for y in range(int(num_rows))] 
        #session["csv"][0][x] = num
        session[col_num] +=(str(num) +" ")

def str_generator(num_rows,col_num):
    session[col_num] = ""
    for x in range(int(num_rows)):
        r_str = rand_str(5)
        session[col_num] += r_str+ " "
def dbl_generator(num_rows,col_num):
    session[col_num] = ""
    for x in range(int(num_rows)):
        num = random.uniform( -2**31, 2**31 )
        session[col_num] +=(str(num) + " ")

@app.route('/', methods = ['GET','POST'])
def file_setup():
    if request.method == "POST":
        num_rows = request.form["num_rows"] #number of rows
        types = []
        types = request.form.getlist("myInputs[]")
        #print ("Number of imputs are ",len(types))
        col_num = 0;
        for col in types:
            if col == "Int":
                int_generator(num_rows,int(col_num))
            if col == "String":
                str_generator(num_rows,int(col_num))
            if col == "Double":
                dbl_generator(num_rows,int(col_num))
            else:
                pass
            col_num +=1

        print("PRINTING COLS HERE")
        for x in range(col_num):
            print session[x]
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




