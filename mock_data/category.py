from models import Category
from faker import Faker

fake = Faker()

def random_category(n_categories=3):
    for _ in range(n_categories):
        Category.create(name=fake.unique.word().title())
