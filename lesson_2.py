from datetime import datetime

from sqlalchemy import create_engine, Integer, String, select, update, delete, insert, DateTime, Date, SMALLINT, \
    SmallInteger, PrimaryKeyConstraint
from sqlalchemy.orm import DeclarativeBase, MappedColumn, mapped_column, Session, Mapped, declarative_base, \
    declared_attr
from sqlalchemy.sql.functions import now


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    @declared_attr
    def __tablename__(cls):
        name = cls.__name__
        if name.endswith('y'):
            name = name[:-1] + 'ie'
        return name.lower() + 's'


class TelegramUser(Base):
    first_name: Mapped[str] = mapped_column(String(255),nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=True)
    username: Mapped[str] = mapped_column(String(255), nullable=True, unique=True)
    addition: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[str] = mapped_column(String(12), unique=True)
    image: Mapped[str] = mapped_column(String(255), nullable=True)
    birth_date: Mapped[datetime] = mapped_column(Date, nullable=True)
    online: Mapped[datetime] = mapped_column(DateTime, server_onupdate=now())



engine = create_engine("postgresql://postgres:1@localhost:5432/sqlalchemy_db", echo=True)

Base.metadata.create_all(engine)




#





class Category(Base):
    name: Mapped[str] = mapped_column(String(255))

    def __str__(self):
        return f"{self.id} - {self.name}"


class Product(Base):
    price: Mapped[int] = mapped_column(SmallInteger)
    name: Mapped[str] = mapped_column(String(255))

    def __str__(self):
        return f"{self.id} - {self.name}"


class User(Base):
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255), default="familya")
    phone: Mapped[str] = mapped_column(String(12), unique=True)
    birth_date: Mapped[datetime] = mapped_column(Date, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_onupdate=now())
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=now())

    def __str__(self):
        return f"{self.id} - {self.first_name}"


engine = create_engine("postgresql://postgres:1@localhost:5432/sqlalchemy_db", echo=True)

Base.metadata.create_all(engine)
Base.metadata.drop_all(engine)

if __name__ == '__main__':
    print(1)

# CREATE
with Session(engine) as session:
    query = insert(Category).values(name="last category").returning(Category.id)
    session.execute(query)
    print(session.scalar(query))
    session.commit()

# READ
with Session(engine) as session:
    # query = select(Category)
    query = select(Category.id, Category.name).filter(Category.id <= 2).order_by(Category.id.desc())
    results = session.scalars(query)
    for i in results:
        print(i)

# # UPDATE
# with Session(engine) as session:
#     query = update(Category).values(name='Kiyim-kechak').filter(Category.id == 2)
#     session.execute(query)
#     session.commit()

# DELETE
with Session(engine) as session:
    query = delete(Category).filter(Category.id == 3)
    session.execute(query)
    session.commit()

# Create
with Session(engine) as session:
    category1 = Category(name='Oziq-ovqat')
    category2 = Category(name='Kiyim')
    # session.add(category1)
    session.add_all([category2, category1])
    session.commit()

# READ
with Session(engine) as session:
    category = session.get(Category, 1)
    print(category)


# UPDATE
with Session(engine) as session:
    category = session.get(Category, 1)
    category.name = 'Texnika'
    session.add(category)
    session.commit()

# UPDATE
with Session(engine) as session:
    category = session.get(Category, 1)
    session.delete(category)
    session.commit()














