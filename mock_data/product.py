from models import Product, Category
from faker import Faker
import random

fake = Faker()

def random_product(n_products=10):
    category_query = Category.select()

    categories = [category.id for category in category_query]

    for _ in range(n_products):
        Product.create(
            name=fake.word().title(),
            price=round(random.uniform(5.0, 500.0), 2),
            quantity=random.randint(1, 100),
            category_id=random.choice(categories),
        )
