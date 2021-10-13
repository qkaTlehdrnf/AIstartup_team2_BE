from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session 
from .. import schemas, database, oauth2
from petmilly_app.repository import picture

get_db = database.get_db

router = APIRouter(
    prefix='/picture',
    tags = ['picture']
)







###111
@router.get('/mypost/{user_name}', response_model=List[schemas.ShowPicture])
async def read_all_pictures_by_blog_id(
    blog_id : int, 
    db: Session = Depends(get_db)
    ):##current_user:schemas.User = Depends(oauth2.get_current_user)
    return picture.read_all_pictures_by_blog_id(blog_id, db)



###222
@router.get('/{user_name}', status_code=200, response_model=schemas.ShowPicture)
async def read_picture_by_picture_id(
    id: int, 
    db: Session = Depends(get_db)
    ):##current_user:schemas.User = Depends(oauth2.get_current_user)
    return picture.read_picture_by_picture_id(id,db)



###333
@router.post('', status_code=status.HTTP_201_CREATED)
async def create(
    request: schemas.Picture, 
    db: Session = Depends(get_db)
    ):##current_user:schemas.User = Depends(oauth2.get_current_user)
    return picture.create(request, db)



###444
@router.delete('/{id}')##203 ERROR HAS SOME ERROR ISSUE
async def delete(
    id: int, 
    db: Session = Depends(get_db)
    ):##current_user:schemas.User = Depends(oauth2.get_current_user)
    return picture.delete(id,db)


