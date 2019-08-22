# pip install faker
import datetime
import random
import time
from faker import Faker
fake = Faker()

from django.contrib.auth.models import User
from genprocandfunctions.models import NhzUsers
('trade_code', 'project_code', 'branch_code', 'user_id', 'user_name', 'pass_word', 'usertype', 'active', 'title', 'cell', 'tele', )
def seed_users(num_entries=10, overwrite=False):
    """
    Creates num_entries worth a new users
    """
    if overwrite:
        print("Overwriting Users")
       NhzUsers.objects.all().delete()
    count = 0
    for _ in range(num_entries):
        first_name = fake.first_name()
        last_name = fake.last_name()
        u = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            email = first_name + "." + last_name + "@fakermail.com",
            username = first_name + last_name,
            password="password"
        )
        count += 1
        percent_complete = count / num_entries * 100
        print(
                "Adding {} new Users: {:.2f}%".format(num_entries, percent_complete),
                end='\r',
                flush=True
                )
    print()