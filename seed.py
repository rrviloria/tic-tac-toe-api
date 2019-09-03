# import django
# import os
# import random
# import decimal
# import uuid

# from datetime import datetime, timedelta
# from django_seed import Seed

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
# django.setup()

# from api.transactions.models import Product, Transaction

# cities = (
#     'Makati City',
#     'Pasig City',
#     'Pasay City',
#     'Marikina City'
# )
# product_names = (
#     'Cheese Classic',
#     'Hawaiian Overload',
#     'Bacon Overload',
#     'Veggies & Cheese Overload'
# )

# products = []
# for name in product_names:
#     product = Product.objects.create(
#         name=name,
#         city=cities[random.randint(0, len(cities) - 1)]
#     )
#     products.append(product)

# seeder = Seed.seeder()
# start = datetime.now()
# end = start - timedelta(days=30)

# seeder.add_entity(Transaction, 75, {
#     'amount': lambda x: decimal.Decimal(random.randrange(100, 400, 30)),
#     'product': lambda x: products[random.randint(0, len(products) - 1)],
#     'date_time': lambda x: start + (end - start) * random.random(),
# })

# seeder.execute()

# print('Seeding complete!')
