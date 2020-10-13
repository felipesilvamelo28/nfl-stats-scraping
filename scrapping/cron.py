from django_cron import CronJobBase, Schedule
from .views import *


class cron_carregar_dados(CronJobBase):
    RUN_EVERY_MINS = 5 # every 5 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'scrapper.my_cron_job'    # a unique code

    def do(self):
        import_data()




