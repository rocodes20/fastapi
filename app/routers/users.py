from fastapi import APIRouter,Depends,HTTPException

from app.db.connection import get_db
from app.schemas.user import UserCreate,UserResponse,UserPatch
from app.services.user_service import create_user,get_user_by_id,patch_user,delete_user

router = APIRouter()

@router.post("/users",response_model=UserResponse)
def create_user_route(user:UserCreate,db = Depends(get_db)):
    return create_user(user,db)

@router.get("users/{user_id}",response_model=UserResponse)
def get_user_router(user_id:int,db = Depends(get_db)):
    user = get_user_by_id(user_id,db)
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    return user

@router.patch("users/{user_id}",response_model=UserResponse)
def patch_user_route(user_id:int,user:UserPatch,db = Depends(get_db)):
    try: 
        patch_user(user_id,user,db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except RuntimeError:
        raise HTTPException(status_code=500, detail="update failed")
    
@router.delete("/users/{user_id}")
def delete_user_route(user_id,db= Depends(get_db)):
    return delete_user(user_id,db)