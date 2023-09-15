from flask import Flask, request
import json
import jobs
import flask

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
   return json.dumps("The server is up and runninggg \n")

@app.route('/test', methods=['GET'])
def test():
   return jobs.test()

@app.route('/jobs/<string:uid>', methods=['GET'])
def get_job(uid):
    return_dict = jobs.return_job(uid)
    return return_dict

@app.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return jobs.add_job(job['start'], job['end'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

