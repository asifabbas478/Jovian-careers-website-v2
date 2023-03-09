from flask import Flask,render_template,jsonify,request
from database import load_jobs_from_db1,load_jobs_from_db2,add_application_to_db

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

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data=request.form
  job=load_jobs_from_db2(id)
  add_application_to_db(id,data)
  return render_template('application_submitted.html',application=data,
                        job=job)
  
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
