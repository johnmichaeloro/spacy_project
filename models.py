import datetime

from peewee import *

DATABASE = MySQLDatabase('quote', user='john', password='PASSword5!')

class Quote(Model):
    text = CharField()
    title = CharField()
    author = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Quote], safe=True)
    DATABASE.close()
