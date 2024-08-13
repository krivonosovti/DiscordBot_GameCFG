# src/database/models.py

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database.db_connection import Base

# Таблица для связи многие-ко-многим между пользователями и играми
user_game_association = Table(
    'user_game_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('game_id', Integer, ForeignKey('games.id'))
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    
    # Связь с таблицей Game через таблицу ассоциаций
    games = relationship("Game", secondary=user_game_association, back_populates="users")

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    
    # Связь с таблицей User через таблицу ассоциаций
    users = relationship("User", secondary=user_game_association, back_populates="games")
    
    # Связь с конфигами
    configs = relationship("Config", back_populates="game")

class Config(Base):
    __tablename__ = 'configs'

    id = Column(Integer, primary_key=True, index=True)
    file_path = Column(String, nullable=False)
    
    # Внешний ключ на таблицу Game
    game_id = Column(Integer, ForeignKey('games.id'))
    
    # Внешний ключ на таблицу User
    user_id = Column(Integer, ForeignKey('users.id'))

    # Связь с таблицами Game и User
    game = relationship("Game", back_populates="configs")
    user = relationship("User")