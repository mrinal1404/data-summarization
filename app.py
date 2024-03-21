from flask import Flask,render_template,url_for
from flask import request as req
import requests
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])

def Index():
       return render_template("index.html")
@app.route("/Summarize",methods=["GET","POST"])
def summarize():
    if req.method=="POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer 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"}
        data=req.form["data"]
    
        minL=30
        maxL=70
    
        def query(payload):
           response = requests.post(API_URL, headers=headers, json=payload)
           return response.json()
        output = query({
	    "inputs":data,
	    "parametres":{"min_length":minL,"max_length":maxL}
                      })
        return render_template("index.html",result=output)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.debug=True
    app.run()

    

