from apscheduler.schedulers.blocking import BlockingScheduler
import GradeScrapper


def job_schedule():
    instance =GradeScrapper.MauaScrapper()
    instance.compare(user = '18.00522-5@maua.br')
    
            


scheduler = BlockingScheduler({'apscheduler.timezone': 'Brazil/East'})

scheduler.add_job(job_schedule, 'cron', hour='*', minute=59)
scheduler.start()
