#!/usr/bin/python
# -*- coding: utf-8 -*-
"""To-Do app powered by Flask."""

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def to_do():
    author = "Me"
    name = "You"
    return render_template('index.html', author=author, name=name)

if __name__ == '__main__':
    app.run()