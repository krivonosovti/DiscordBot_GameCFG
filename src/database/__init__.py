from database.db_connection import engine
from database.models import Base

# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)
