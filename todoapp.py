#!/usr/bin/python
# -*- coding: utf-8 -*-
"""To-Do app powered by Flask."""

from flask import Flask, render_template, request, redirect
app = Flask(__name__)


if __name__ == '__main__':
    app.run()