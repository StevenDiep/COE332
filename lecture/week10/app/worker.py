from jobs import q, update_job_status
import time
import os

worker_ip = os.environ.get('WORKER_IP')
if not worker_ip:
    raise Exception()

@q.worker   # fill in
def execute_job(jid):
    update_job_status(jid, "in progress")
    time.sleep(15)
    update_job_status(jid, "completed by " + worker_ip)

execute_job()
