from flask import Flask, render_template, session, redirect, url_for, make_response
from flask import request
import random


app = Flask(__name__)
  
#global for session data, sessions are sometimes not persistent
gSessionData ={}
# make matrix of strings and append to it str(int) str(double) str(char) str(date)
# then we can simple rotate it to produce the file
def rand_str(length):
    alphanum = 'abcdefghijklmnopqrstuvwxyz0123456789'
    id = ''
    for i in range(length):
        id += random.choice(alphanum)
    return id

def int_generator(num_rows,col_num):
    session[col_num] = []
    for x in range(int(num_rows)):
        num = random.randint(-2**31,2**31)
        #session[col_num] +=(str(num) +" ")
        session[col_num].append(str(num))

    gSessionData[col_num]  =session[col_num]

def str_generator(num_rows,col_num):
    session[col_num] = []
    for x in range(int(num_rows)):
        r_str = rand_str(5)
        session[col_num].append(r_str)

    gSessionData[col_num]  =session[col_num]


def dbl_generator(num_rows,col_num):
    session[col_num] = []
    for x in range(int(num_rows)):
        num = random.uniform( -2**31, 2**31 )
        session[col_num].append(str(num))

    gSessionData[col_num]  =session[col_num]


def session_print(col_num):
    print "IN SESSION"
    print ("Size is ",col_num)
    for x in range(col_num):
            try:
                print session[str(x)]
            except:
                pass


###############################################################################################################

############################################# MAIN ROUTES #####################################################



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

        session["col_num"] = col_num
        # print("PRINTING COLS HERE")

        # for x in range(col_num):
        #     try:
        #         print session[x]
        #     except:
        #         pass
        #session_print(session["col_num"])
        return redirect (url_for("file_out"))

    return render_template("home.html") #html for page




@app.route('/file_out')
def file_out():
    # We need to modify the response, so the first thing we
    # need to do is create a response out of the CSV string
    # 2D list
    elements = []
    for x in range(session["col_num"]):
        elements.append([])

    print "in last route"
    #ession_print(session["col_num"])
    try:
        #print ("HIHIH",gSessionData)
        pass
    except:
        pass
    
    # trylist = gSessionData[0]
    # print trylist
    # print trylist[0]
    
    print gSessionData
    for x in range(session["col_num"]):
        elements[x] = gSessionData[x]

    # elements[0] = gSessionData[0]
    # elements[1] = gSessionData[1]
    # print("NOW PRINITNG FINAL")
    # print elements[0]
    # print elements[1]

    for val in elements:
        print val
    
    # csv = ""
    # for key in elements[0]:
    #     csv += key +" "
    # print("CSV IS ", csv)

    return "HI"
    #response = make_response(csv)
    # This is the key: Set the right header for the response
    # to be downloaded, instead of just printed on the browser
    #response.headers["Content-Disposition"] = "attachment; filename=response.txt"
    #return response



if __name__ == '__main__':
    app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'
    app.run(debug = 'True')




