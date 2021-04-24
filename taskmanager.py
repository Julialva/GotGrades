from apscheduler.schedulers.blocking import BlockingScheduler
import main


def job_schedule():
    instance =MauaScrapper()
    instance.compare(user = '18.00522-5@maua.br')
    
            


scheduler = BlockingScheduler({'apscheduler.timezone': 'Brazil/East'})

scheduler.add_job(job_schedule, 'cron', hour='*', minute=1)
scheduler.start()
