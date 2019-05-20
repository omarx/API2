from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/')

def just_test():
    return("Hello World")

app.run(port=5000)
