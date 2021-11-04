from typing import List
from sqlalchemy.orm import Session
from .. import models, database, JWTtoken
from fastapi import APIRouter, Depends, status, HTTPException
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm as OAuth2Form

get_db=database.get_db

router = APIRouter(tags=['authentication'])

@router.post('/login')
def login(request: OAuth2Form = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    
    if not user:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Incorrect Password")
    
    access_token = JWTtoken.create_access_token(data={"sub": user.email})
    return {"access_token":access_token,"token_type":"bearer"}