from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session 
from .. import schemas, database, oauth2
from petmilly_app.repository import comment

get_db = database.get_db

router = APIRouter(
    prefix='/comment',
    tags = ['Comment']
)







###111
@router.get('/mypost/{user_name}', response_model=List[schemas.ShowComment])
async def read_all_comments_by_blog_id(
    user_id : int, 
    db: Session = Depends(get_db)
    ):##current_user:schemas.User = Depends(oauth2.get_current_user)
    return comment.read_all_comments_by_blog_id(user_id, db)



###222
@router.get('/{user_name}', status_code=200, response_model=schemas.ShowComment)
async def read_comment_by_comment_id(
    id: int, 
    db: Session = Depends(get_db)
    ):##current_user:schemas.User = Depends(oauth2.get_current_user)
    return comment.read_comment_by_comment_id(id,db)



###333
@router.post('', status_code=status.HTTP_201_CREATED)
async def create(
    request: schemas.Comment, 
    db: Session = Depends(get_db)
    ):##current_user:schemas.User = Depends(oauth2.get_current_user)
    return comment.create(request, db)



###444
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    id: int, 
    db: Session = Depends(get_db)
    ):##current_user:schemas.User = Depends(oauth2.get_current_user)
    return comment.delete(id,db)


