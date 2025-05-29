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
