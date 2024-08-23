from flask import Flask,render_template,request
from Controller import getdata

app = Flask (__name__)

@app.route("/",methods =["POST","GET"] )

def myUniverse():
    resposne = getdata()
    return resposne


if __name__ == "__main__":
    app.run(debug= True,port= 8080)
