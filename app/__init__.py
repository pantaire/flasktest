from flask import Flask, render_template, flash, redirect, request, session, abort

app = Flask(__name__)

from app import routes



if __name__ == "__main__": 
    app.run()