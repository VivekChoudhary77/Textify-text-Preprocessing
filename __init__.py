from flask import Flask, redirect, url_for, request ,render_template
from main import *
from text_generate import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/text-generator')
def text_generator():
    return render_template("text_generator.html")

@app.route('/output',methods=['POST'])
def output():
    if request.method == 'POST':
        textvalue = request.form.get("textarea", None)
        return render_template('Output_Content.html', res=outputsumm(textvalue))

@app.route('/outputgen',methods=['POST'])
def output_generator():
    if request.method == 'POST':
        textvalue = request.form.get("textarea_ofinp", None)
        return render_template('text_generator.html', reret=textvalue, ret=output_generate(textvalue))

if __name__ == '__main__':
    app.run(debug=True)
