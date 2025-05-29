from models import User
from faker import Faker

fake = Faker()

def random_user(n_users=5):
    for _ in range(n_users):
        User.create(name=fake.name(), birthday=fake.date_of_birth())
