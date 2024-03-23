from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from model import *

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost",]
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,



    allow_methods=["*"],



    allow_headers=["*"],)


class ProductSchema(BaseModel):
    name:str
    image:str
    price:int
    users_id:int
    sellers_id:int

    class Config:
        orm_mode=True


class OptionProductSchema(BaseModel):
    name:Optional[str]
    image:Optional[str]
    price:Optional[str]
    users_id:Optional[int]
    sellers_id:Optional[int]

    class Config:
        orm_mode=True

class Userschema(BaseModel):
    name:str
    username:str
    password:str

    class Config:
        orm_mode=True

class OptionUserSchema(BaseModel):
    name: Optional[str]
    username: Optional[str]
    password: Optional[str]
    class Config:
        orm_mode=True

class Sellerschema(BaseModel):
    name:str
    username:str
    password:str

    class Config:
        orm_mode=True

class OptionSellersSchema(BaseModel):
    name: Optional[str]
    username: Optional[str]
    password: Optional[str]
    class Config:
        orm_mode=True
    
    


@app.get('/products')
def getproducts():
    return session.query(Products).all()

@app.get('/products/{id}')
def getproduct(id:int):
    return session.query(Products).filter_by(id=id).first()

@app.post('/addproduct')
def addproduct(products:ProductSchema):
    product= Products(**dict(products))
    session.add(product)
    session.commit()
    return {"detail":"Added successfully"}



@app.delete('/deleteproduct/{id}')
def deleteproduct(id:int) -> None:
    product = session.query(Products).filter_by(id=id).first()
    session.delete(product)
    session.commit()
    return {"detail":f"product with id {id} deleted successfully"}

@app.put('/putproduct/{id}')
def productPut(id:int, payload:OptionProductSchema):
    product = session.query(Products).filter_by(id=id).first()
    for key, value in dict(payload).items():
        setattr(product, key, value)
    session.commit()
    return {"detail":f"product with id {id} updated successfully"}



@app.patch('/patchproduct/{id}')
def productpatch(id:int, payload:OptionProductSchema):
    product = session.query(Products).filter_by(id=id).first()
    for key, value in dict(payload).items():
        setattr(product, key, value)
    session.commit()
    return {"detail":f"product with id {id} updated successfully"}


@app.get('/users')
def getusers():
    return session.query(Users).all()

@app.get('/users/{id}')
def getuser(id:int):
    return session.query(Users).filter_by(id=id).first()

@app.post('/addusers')
def addusers(users:Userschema):
    user= Users(**dict(users))
    session.add(user)
    session.commit()
    return {"detail":"Added successfully"}



@app.delete('/deleteusers/{id}')
def deleteusers(id:int) -> None:
    users = session.query(Users).filter_by(id=id).first()
    session.delete(users)
    session.commit()
    return {"detail":f"users with id {id} deleted successfully"}

@app.put('/putusers/{id}')
def usersPut(id:int, payload:OptionUserSchema):
    users = session.query(Users).filter_by(id=id).first()
    for key, value in dict(payload).items():
        setattr(users, key, value)
    session.commit()
    return {"detail":f"users with id {id} updated successfully"}



@app.patch('/patchusers/{id}')
def userspatch(id:int, payload:OptionUserSchema):
    users = session.query(Users).filter_by(id=id).first()
    for key, value in dict(payload).items():
        setattr(users, key, value)
    session.commit()
    return {"detail":f"users with id {id} updated successfully"}


@app.get('/sellers')
def getsellers():
    return session.query(Sellers).all()

@app.get('/sellers/{id}')
def getseller(id:int):
    return session.query(Sellers).filter_by(id=id).first()

@app.post('/addsellers')
def addsellers(sellers:Sellerschema):
    seller= Sellers(**dict(sellers))
    session.add(seller)
    session.commit()
    return {"detail":"Added successfully"}



@app.delete('/deletesellers/{id}')
def deletesellers(id:int) -> None:
    sellers = session.query(Sellers).filter_by(id=id).first()
    session.delete(sellers)
    session.commit()
    return {"detail":f"sellers with id {id} deleted successfully"}

@app.put('/putsellers/{id}')
def sellersPut(id:int, payload:OptionSellersSchema):
    sellers = session.query(Sellers).filter_by(id=id).first()
    for key, value in dict(payload).items():
        setattr(sellers, key, value)
    session.commit()
    return {"detail":f"sellers with id {id} updated successfully"}



@app.patch('/patchsellers/{id}')
def sellerspatch(id:int, payload:OptionSellersSchema):
    sellers = session.query(sellers.filter_by(id=id).first())
    for key, value in dict(payload).items():
        setattr(sellers, key, value)
    session.commit()
    return {"detail":f"sellers with id {id} updated successfully"}