from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

# Получение данных для подключения к базе данных из переменных окружения
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL не установлена в .env файле")

# Создание движка SQLAlchemy для работы с PostgreSQL
engine = create_engine(DATABASE_URL, echo=True)

# Создание базового класса для описания моделей
Base = declarative_base()

# Создание сессии для взаимодействия с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Получение новой сессии базы данных.
    Используется как зависимость в других модулях, чтобы получить доступ к БД.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Пример использования
if __name__ == "__main__":
    # Создание сессии
    with get_db() as session:
        print("Подключение к базе данных успешно установлено!")
