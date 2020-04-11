from django.core.management import BaseCommand
from django.forms import model_to_dict

from scraping.management.employee_processor import EmployeeProcessor
from scraping.models import Job, Employee


class Command(BaseCommand):

    def _get_jobs(self):
        jobs = []
        for job in Job.objects.all():
            jobs.append(model_to_dict(job))
        return jobs

    def handle(self, *args, **options):
        jobs = self._get_jobs()
        employee_processor = EmployeeProcessor(jobs)
        for employee in Employee.objects.filter(status='active'):
            employee_processor.run(employee)
