from flask import Flask,render_template,jsonify
from database import load_jobs_from_db1,load_jobs_from_db2

app = Flask(__name__)


  

@app.route("/")
def hello_world():
  result_dict_list=load_jobs_from_db1()
  return render_template('home.html', jobs=result_dict_list)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

@app.route("/jobs/<id>")
def show_jobs(id):
  job=load_jobs_from_db2(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html',job=job)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
