from django.core.management import BaseCommand

from scraping.management.employee_processor import EmployeeProcessor
from scraping.management.parse import get_jobs
from scraping.models import Employee


class Command(BaseCommand):

    def _process_employee(self, employee):
        EmployeeProcessor(employee).run()

    def handle(self, *args, **options):
        jobs = get_jobs(10, False)
        employee_processor = EmployeeProcessor(jobs)
        for employee in Employee.objects.filter(status='active'):
            employee_processor.run(employee)
