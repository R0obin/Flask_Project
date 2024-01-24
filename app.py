from flask import Flask,render_template,redirect,url_for,request
import pandas as pd
app = Flask(__name__)



@app.route('/success/<int:score>')
def success(score):
    return render_template('submit.html',result=score)
@app.route('/fail/<int:score>')
def fail(score):
    return "Your registration has been failed" +str(score)

@app.route('/form',methods=["POST","GET"])
def form():
    if request.method=="GET":
        return render_template("index.html")
    else:
        math = float(dict(request.form)['maths'])
        science = float(dict(request.form)['science'])
        history = float(dict(request.form)['history'])
    Total_percentage = (math + science + history) / 3
    
    return render_template("submit.html",score= Total_percentage)

    # res = ''
    # if Total_percentage < 35:
    #     res = "fail"
    # else:
    #     res = "success"
    # return redirect(url_for(res,score=Total_percentage))
    

@app.route('/submit')
def submit():
    redirect(url_for('success'))




    
            



if __name__=='__main__':
    app.run(debug=True)






