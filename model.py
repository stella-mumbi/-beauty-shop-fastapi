from sqlalchemy import Column, Integer, String, Table, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


Base = declarative_base()

# product_user = Table(
#     'product_user',
#     Base.metadata,
#     Column('product_id',Integer, ForeignKey('product.id'), primary_key=True),
#     Column('users_id',Integer, ForeignKey('users.id'), primary_key=True),
#     Column('sellers_id',Integer, ForeignKey('sellers.id'), primary_key=True),
#     extend_existing=True,

# )

class Products(Base):
    __tablename__="product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(), nullable=False)
    image = Column(String(), nullable=False)
    price = Column(Integer(), nullable=False)

    users_id=Column(Integer(), ForeignKey("users.id"))
    sellers_id=Column(Integer(),  ForeignKey("sellers.id"))

    users = relationship('Users',  backref="product")
    sellers = relationship('Sellers', backref="product")

class Users(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(), nullable=False)
    username=Column(String(),nullable=False)
    password=Column(String(),nullable=False)


    # products = relationship('Products', secondary=product_user, back_populates='users')

class Sellers(Base):
    __tablename__="sellers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(), nullable=False)
    username=Column(String(),nullable=False)
    password=Column(String(),nullable=False)

    # products = relationship('Products', secondary=product_user, back_populates='sellers')


engine = create_engine('sqlite:///beauty.db', connect_args={"check_same_thread":False})
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
