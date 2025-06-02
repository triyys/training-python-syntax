## Tạo database với mysql
### 1. Tải và bật mysql (macOS)
```bash
brew services start mysql
```
### 2. Tải Peewee và MySQL Driver
```bash
pip install peewee mysqlclient
```
### 3. Định nghĩa database connection
`models/database.py`
```python
from peewee import Model, MySQLDatabase

db = MySQLDatabase(
    'training_python_peewee',
    user='root',
    # password='',
    host='localhost',
    port=3306
)

class BaseModel(Model):
    class Meta:
        database = db
```
### 4. Định nghĩa các model
`models/user.py`
`models/product.py`
`models/category.py`
`models/order.py`

Trong đó:
```python
from peewee import CharField, AutoField, DateField # ...
```
là các class dùng để ánh xạ đến các thuộc tính của các cột trong database
[fields](https://docs.peewee-orm.com/en/latest/peewee/models.html#fields)
```python
class Meta:
    table_name = 'users'
```
để định nghĩa lại tên bảng lưu dưới database
[Metadata.set_table_name](https://docs.peewee-orm.com/en/latest/peewee/api.html#Metadata.set_table_name),
mặc định sẽ là tên model viết thường (user) nếu không định nghĩa
### 5. Kết nối đến mysql và tạo bảng
```python
from peewee import OperationalError
from models import db, User, Category, Product, Order

try:
    db.connect()
    db.create_tables([User, Category, Product, Order])
    print('Tables created successfully!')
except OperationalError as e:
    print(f'Failed to connect to DB: {e}')
finally:
    if not db.is_closed():
        db.close()
        print('Database connection closed.')
```

## Insert dữ liệu vào database
Thêm 1 người dùng
```python
from models import User
from datetime import date

User.create(name='Tri Ngo', birthday=date(2001, 12, 25))
```

## Viết select và where đơn giản
Lấy ra các `Product` có số hàng tồn kho là 15
```python
from models import Product

query = Product.select().where(Product.quantity == 15)

[print(f'{product.id}: {product.name} {product.price}') for product in query]
```

## Viết join cơ bản
Lấy ra các `Product` cùng với thông tin `Category` tương ứng và có id loại sản phẩm là 3
```python
from models import Product, Category

query = (Product
         .select(Product, Category)
         .join(Category)
         .where(Product.category_id == 3))

[print(f'{product.id}: {product.name} {product.price}') for product in query]
```
