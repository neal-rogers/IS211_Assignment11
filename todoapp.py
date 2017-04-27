#!/usr/bin/python
# -*- coding: utf-8 -*-
"""To-Do app powered by Flask."""

import re
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

tasks = []

@app.route('/')
def to_do():
    author = "Neal Rogers"
    return render_template('index.html', author=author)

@app.route('/submit', methods= ['POST'])
def submit():
    desc = request.form['task']
    priority = request.form['priority']
    email = request.form['email']
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return render_template('index.html')
    else:
        tasks.append(desc, priority, email)
        return render_template('index.html')

if __name__ == '__main__':
    app.run()