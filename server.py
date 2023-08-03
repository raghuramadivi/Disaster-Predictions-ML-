from flask import Flask,render_template,request

app = Flask(__name__)

#Index page, no args
@app.route('/')
def index():
    return render_template('dashboard.html')

#With debug=True, Flask server will auto-reload
#... When there are code changes 
if __name__=='__main__': #That's how we define main function in python
     app.run(port=5000,debug=True)
