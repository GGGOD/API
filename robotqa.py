# house3.py
from flask import Flask,jsonify,request, render_template
from wtforms import Form, TextAreaField, validators
from getQA import getQA
from getREC import getREC
from getMedical import getMedical
from getREC import getREC
app=Flask(__name__)


class HelloForm(Form):
    question = TextAreaField('', [validators.DataRequired()])

@app.route("/")
def index():
    form  =  HelloForm(request.form)
    return render_template('first_app.html', form=form)

@app.route("/med/")
def index2():
    form  =  HelloForm(request.form)
    return render_template('second_app.html', form=form)

@app.route("/rec/")
def index3():
    form  =  HelloForm(request.form)
    return render_template('third_app.html', form=form)


@app.route("/medical/", methods=['POST'])
def getMed():
    if request.method=='POST':
        question=request.form['question']
        res = getMedical(question)
        #return jsonify({"data":res})
        return render_template('hello2.html', name= res)

@app.route("/question/", methods=['POST'])
def getAPI():
    if request.method=='POST':
        question=request.form['question']
        res = getQA(question)
        #return jsonify({"data":res})
        return render_template('hello.html', name= res)

@app.route("/recommendation/", methods=['POST'])
def getRec():
    if request.method=='POST':
        question=request.form['question']
        res = getREC(question)
        return render_template('hello3.html', name= res)
    
if __name__=="__main__":
    app.run('0.0.0.0')
