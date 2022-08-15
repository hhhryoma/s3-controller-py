from datetime import datetime
import time
import schedule



def job(job_name):
    print(datetime.now())
    print(f'exec job {job_name}')
    time.sleep(30)
    
# ランダムな間隔でジョブ実行
def schedule_random(f, t, fanc, **func_args):
    schedule.every(f).to(t).seconds.do(fanc, **func_args)

# 一定間隔でジョブ実行
def schedule_every(sec, fanc, **func_args):
    schedule.every(sec).seconds.do(fanc, **func_args)


# exec_random = schedule_random(job, job_name='job test')
# exec_ok = True
# while True:
#     if exec_ok:
#         schedule.run_pending()
#     else:
#         schedule.cancel_job(exec_random)
    
