from sqlalchemy import create_engine,text
import os
db_connection_string = os.environ['DB_CONNECTION_STRING']
engine= create_engine(db_connection_string,
                      connect_args={
                        "ssl":{
                          "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      })

def load_jobs_from_db1():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    columns = ['id', 'title', 'location', 'salary', 'currency', 'job_description', 'job_qualifications']
    result_dict_list = [dict(zip(columns, row)) for row in result.all()]
  return result_dict_list

def load_jobs_from_db2(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id = :id"), {"id": id})
        rows = result.all()
        if len(rows) == 0:
            return None 
        else:
            columns = ['id', 'title', 'location', 'salary', 'currency', 'job_description', 'job_qualifications']
            return dict(zip(columns, rows[0]))
