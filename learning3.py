# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 09:39:00 2023

@author: student
"""

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

songs = []

class Song(db.Model):
    songId = db.Column('songId', db.Integer, primary_key = True)
    Title = db.Column(db.String(100))
    Artist = db.Column(db.String(100))
    Album = db.Column(db.String(100))
    Genre = db.Column(db.String(100))
    Track = db.Column(db.Integer)
    Year = db.Column(db.String(100))
    
@app.route('/')
def home():
    print("here")
    songs = Song.query.all()
    print(songs)
    return render_template('base.html', songs=songs)

if __name__ == '__main__':
    app.run()
    