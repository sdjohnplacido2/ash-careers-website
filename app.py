from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Baliuag, Bulacan',
        'salary': 'php 20,000'
    },
    {
        'id': 2,
        'title': 'Data Science',
        'location': 'San Rafael, Bulacan',
        'salary': 'php 25,000'
    },
    {
        'id': 3,
        'title': 'Data Engineer',
        'location': 'Tiaong, Bulacan',

    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Jose, Bulacan',
        'salary': 'php 100,000'
    }
]


@app.route("/")
def hello_world():
    joblist = load_jobs_from_db()
    return  render_template('home.html',
                            jobs=joblist,
                            company_name="Assshhh")  #"<h1>I love Reg!</h1>"

@app.route("/api/jobs")
def list_jobs():
    return jsonify(joblist=load_jobs_from_db())

if __name__ == "__main__":
    app.run(debug=True)