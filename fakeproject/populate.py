
import os
import django
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakeproject.settings')
django.setup()

from faker import Faker
from myapp.models import employee
f=Faker('en_IN')

def generate_populate(n):
    for i in range(n):
        fname=f.name()
        femail=f.email()
        fposition=f.job()
        fsalary=Decimal(f.random_int(min=30000, max=100000))
        employee.objects.get_or_create(name=fname, email=femail, position=fposition, salary=fsalary)
generate_populate(20)