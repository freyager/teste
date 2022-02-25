from flask import Flask
from pkg_resources import Requirement
from webbrowser import views

app=Flask(__name__)
app.register_blueprint (views,url_prefix="/")
if __name__=="__main__":
    app.run (debug=True, port=8000)
