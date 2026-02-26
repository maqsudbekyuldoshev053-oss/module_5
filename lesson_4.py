
 import csv
from datetime import datetime

from sqlalchemy import create_engine, Integer, String, DateTime, ForeignKey, insert
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, declared_attr, relationship, Session
from sqlalchemy.sql.functions import now


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    @declared_attr
    def __tablename__(cls):
        name = cls.__name__[0].lower()

        for i in cls.__name__[1:]:
            if i.isupper():
                name += '_' + i.lower()
            else:
                name += i

        if name.endswith('y'):
            name = name[:-1] + 'ie'
        return name.lower() + 's'




class User(Base):
    first_name: Mapped[str] = mapped_column(String(255))
    phone: Mapped[str] = mapped_column(String(15), unique=True)


class Course(Base):
    


















