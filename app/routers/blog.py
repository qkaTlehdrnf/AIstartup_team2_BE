from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session 
from .. import schemas, database, oauth2
from .. repository import blog

get_db=database.get_db

router = APIRouter(
    prefix="/blog",
    tags = ['Blog']
)







###111
@router.get('/mypost/{user_name}', response_model=List[schemas.ShowBlog])
async def read_all_blogs_by_user_id(
    user_id : int, 
    db: Session = Depends(get_db)
    ):##current_user:schemas.User = Depends(oauth2.get_current_user)
    return blog.read_all_blogs_by_user_id(user_id, db)



###222
@router.get('/{user_name}', status_code=200, response_model=schemas.ShowBlog)
async def read_blog_by_blog_id(
    id: int, 
    db: Session = Depends(get_db)
    ):##current_user:schemas.User = Depends(oauth2.get_current_user)
    return blog.read_blog_by_blog_id(id,db)
    


###333
@router.post('', status_code=status.HTTP_201_CREATED)
async def create(
    request: schemas.Blog, 
    db: Session = Depends(get_db)
    ):##current_user:schemas.User = Depends(oauth2.get_current_user)
    return blog.create(request, db)



###444
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update(
    id: int, request: schemas.Blog, 
    db: Session = Depends(get_db)
    ):#current_user:schemas.User = Depends(oauth2.get_current_user)
    return blog.update(id,request,db)



###555
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    id: int, 
    db: Session = Depends(get_db)
    ):##current_user:schemas.User = Depends(oauth2.get_current_user)
    return blog.delete(id,db)