from django.core.management import BaseCommand

from scraping.management.employee_processor import EmployeeProcessor
from scraping.models import Employee


class Command(BaseCommand):

    def _process_employee(self, employee):
        pass
        EmployeeProcessor(employee).run()

    def handle(self, *args, **options):
        for employee in Employee.objects.filter(status='active'):
            self._process_employee(employee)
