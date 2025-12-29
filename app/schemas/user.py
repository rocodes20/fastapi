from pydantic import BaseModel
class UserCreate(BaseModel):
    name:str
    email:str

class UserResponse(BaseModel):
    id:int
    name:str | None = None
    email:str | None = None

class UserPatch(BaseModel):
    name: str | None = None
    email: str | None = None