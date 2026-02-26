import csv
from datetime import datetime

from sqlalchemy import create_engine, Integer, String, DateTime, ForeignKey, insert
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, declared_attr, relationship, Session
from sqlalchemy.sql.functions import now


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    @declared_attrf
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


class Category(Base):
    name: Mapped[str] = mapped_column(String(255))
    slug: Mapped[str] = mapped_column(String(255), unique=True)
    adverts: Mapped[list['Advert']] = relationship('Advert', back_populates='category')

    def __str__(self):
        return f"{self.id} - {self.name}"


class Advert(Base):
    name: Mapped[str] = mapped_column(String(255))
    slug: Mapped[str] = mapped_column(String(255), unique=True)
    price: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String(15))
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    category: Mapped['Category'] = relationship('Category', back_populates='adverts')

    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    owner: Mapped['User'] = relationship('User', back_populates='adverts')

    view_count: Mapped[int] = mapped_column(Integer, server_default='0')
    published_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_onupdate=now())
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=now())

    images: Mapped[list['AdvertImage']] = relationship('AdvertImage', back_populates='advert')


class AdvertImage(Base):
    image: Mapped[str] = mapped_column(String(255))
    advert_id: Mapped[int] = mapped_column(ForeignKey('adverts.id'))
    advert: Mapped['Advert'] = relationship('Advert', back_populates='images')


class User(Base):
    first_name: Mapped[str] = mapped_column(String(255))
    phone: Mapped[str] = mapped_column(String(15), unique=True)
    last_login: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_onupdate=now())
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=now())

    adverts: Mapped[list['Advert']] = relationship('Advert', back_populates='owner')




class Region(Base):
    name: Mapped[str] = mapped_column(String(255))
    districts: Mapped[list['District']] = relationship('District', back_populates='region')
    users: Mapped[list['User']] = relationship('User', back_populates='region')


class District(Base):
    name: Mapped[str] = mapped_column(String(255))
    region_id: Mapped[int] = mapped_column(ForeignKey('regions.id'))
    region: Mapped['Region'] = relationship('Region', back_populates='districts')

    users: Mapped[list['User']] = relationship('User', back_populates='district')


pg_url="postgresql://postgres:1@localhost:5432/sqlalchemy_db"
engine = create_engine(pg_url)

Base.metadata.create_all(engine)



with open('regions.csv', 'r') as f1, Session(engine) as session:
    regions = csv.DictReader(f1)
    query = insert(Region).values(list(regions))
    session.execute(query)
    session.commit()


with open('districts.csv', 'r') as f1, Session(engine) as session:
    regions = csv.DictReader(f1)
    query = insert(District).values(list(regions))
    session.execute(query)
    session.commit()

