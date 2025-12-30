from pydantic import BaseModel, Field
class UserCreate(BaseModel):
    name:str
    email:str
    password : str = Field(min_length=8, max_length=72)

class UserResponse(BaseModel):
    id:int
    name:str | None = None
    email:str | None = None

class UserPatch(BaseModel):
    name: str | None = None
    email: str | None = None