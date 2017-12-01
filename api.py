# house3.py
from flask import Flask,jsonify,request
from getQA import getQA
app=Flask(__name__)

@app.route("/question/", methods=['POST'])
def getAPI():
    if request.method=='POST':
        question=request.form['question']
        res = getQA(question)
        return jsonify({"data":res})
    
if __name__=="__main__":
    app.run('0.0.0.0')
