from flask import Flask, render_template, redirect, session

app=Flask(__name__)

@app.route('/')
