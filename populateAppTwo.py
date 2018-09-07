import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import User
from faker import Faker


fakegen = Faker()

def populate(N=5):

    for item in range(N):
        # Create the fake data for entry
        fName = fakegen.first_name()
        lName = fakegen.last_name()
        eM = fakegen.email()
        # Creare the new
        user = User.objects.get_or_create(firstName=fName,lastName=lName,email=eM)[0]

if __name__ == '__main__':
    print('Initializing Populating!')
    populate(20)
    print('Populating Finished!')
