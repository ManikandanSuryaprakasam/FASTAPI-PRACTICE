from typing import List, Optional

from fastapi.responses import HTMLResponse, PlainTextResponse                                                                                
from schemas import ArticleBase, ArticleDisplay
from sqlalchemy.orm import Session
from fastapi import APIRouter, Cookie, Depends, Form, Header, Response
from db.database import get_db
from db import db_article 
from fastapi.params import Depends
from auth.oauth2 import get_current_user
from schemas import UserBase



router = APIRouter(
    prefix="/product",
    tags=['product']
)

# How to add the different types of responses in openapi documentation
products = ['watch', 'phone', 'laptop']


#Form data 
@router.post('/new')
def create_product(name:str=Form(...),current_user: UserBase = Depends(get_current_user)):
    products.append(name)   
    return {'data':products,
            'Message': 'Product created successfully'}


#How to add the headers in request and response
@router.get('/withheader')
def get_products(
  
    response:Response,
    # Adding custom headers in request
    custom_header : Optional[List[str]] = Header(None),current_user: UserBase = Depends(get_current_user)
    ):
    # To set the cookie we need to run this request 
    response.set_cookie(key="test_cookie", value="Iam_your_Cookie_how_are_you")
    response.headers['custom_response_header']  = " and ".join(custom_header)
    return products


#How to return header,Cookies in response


#How to add the headers in request and response
@router.get('/withcookie')
def get_products(
  
    response:Response,
    # Adding custom headers in request
    custom_header : Optional[List[str]] = Header(None),
    test_cookie: Optional[str] = Cookie(None),
    current_user: UserBase = Depends(get_current_user)
    ):
    if custom_header:
        response.headers['custom_response_header']  = " and ".join(custom_header)
    return {'data': products, 
            'custom_header': custom_header,                        
            'test_cookie': test_cookie}




@router.get('/all')
def get_all_products(current_user: UserBase = Depends(get_current_user)):
    data = " ".join(products)
    return Response(content=data,media_type="text/plain")


@router.get('/{id}',responses={200: {"content": {"text/html": {"example": "<Head><title>Product</title></Head><Body><h1>Product</h1></Body>"}}, "description":"Get Product by ID"},
                               404: {"content": {"text/plain": {"example":"Product Not Found"}},"description":"Product not found"}})
def get_product(id: int,current_user: UserBase = Depends(get_current_user)):
    if id < 0 or id >= len(products):
        out = "Product Not Found"
        return PlainTextResponse(status_code=404, content=out, media_type="text/plain")
    else:
        product = products[id]
        out = f"""
        <Head>
            <style>
            .product {{
                width: 300px;
                height: 200px; 
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 16px;
                margin: 16px;
                display: inline-block;
            }}
            </style>
     </Head>
        <Body>
            <div class="product">{product}</div>        
        </Body>
        """
        return HTMLResponse(content=out, media_type="text/html")