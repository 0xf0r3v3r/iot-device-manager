import os

from peewee import *

db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')

db = PostgresqlDatabase(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=5432
)
