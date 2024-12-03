from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id: Optional[int] = None  # Correctly annotate with Optional type
    username: str  # Mandatory field
    email: str     # Mandatory field
    password: str  # Mandatory field
    is_staff: Optional[bool] = False  # Optional, with a default value
    is_active: Optional[bool] = True  # Optional, with a default value

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "password",
                "is_staff": False,
                "is_active": True
            }
        }


class LoginModel(BaseModel):
    username:str
    password:str


class Settings(BaseModel):
    authjwt_secret_key:str='da041e879eab2171874456ef66ba4a9708df2c178bbe2bd1e7c210f041636481'





class OrderModel(BaseModel):
    id:Optional[int]
    quantity:int
    order_status:Optional[str]="PENDING"
    pizza_size:Optional[str]="SMALL"
    user_id:Optional[int]


    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "quantity":2,
                "pizza_size":"LARGE"
            }
        }


class OrderStatusModel(BaseModel):
    order_status:Optional[str]="PENDING"

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "order_status":"PENDING"
            }
        }