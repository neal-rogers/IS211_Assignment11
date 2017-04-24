#!/usr/bin/python
# -*- coding: utf-8 -*-
"""To-Do app powered by Flask."""

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

tasks = []

@app.route('/')
def to_do():
    author = "Neal Rogers"
    return render_template('index.html', author=author)

@app.route('/submit', methods = ['POST'])
def add_task():
    task = request.form['task']
    priority = request.form['priority']
    email = request.form['email']
    return redirect('/')

if __name__ == '__main__':
    app.run()