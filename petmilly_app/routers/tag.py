from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session 
from .. import schemas, database, oauth2
from petmilly_app.repository import tag

get_db = database.get_db

router = APIRouter(
    prefix='/tag',
    tags = ['tag']
)







###111
@router.get('/{blog_id}', response_model=List[schemas.ShowTag])
async def read_all_tags_by_blog_id(
    blog_id : int, 
    db: Session = Depends(get_db)
    ):##current_user:schemas.User = Depends(oauth2.get_current_user)
    return tag.read_all_tags_by_blog_id(blog_id, db)



###222
@router.get('/{user_name}', status_code=200, response_model=schemas.ShowTag)
async def read_tag_by_tag_id(
    id: int, 
    db: Session = Depends(get_db)
    ):##current_user:schemas.User = Depends(oauth2.get_current_user)
    return tag.read_tag_by_tag_id(id,db)



###333
@router.get('/mypost/{user_name}', response_model=List[schemas.ShowTag])
async def read_all_blogs_by_tag_id(
    tag_id : int, 
    db: Session = Depends(get_db)
    ):##current_user:schemas.User = Depends(oauth2.get_current_user)
    return tag.read_all_blogs_by_tag_id(tag_id, db)




###444
@router.post('', status_code=status.HTTP_201_CREATED)
async def create(
    request: schemas.tag, 
    db: Session = Depends(get_db)
    ):##current_user:schemas.User = Depends(oauth2.get_current_user)
    return tag.create(request, db)



###555
@router.delete('/{id}')##203 ERROR HAS SOME ERROR ISSUE
async def delete(
    id: int, 
    db: Session = Depends(get_db)
    ):##current_user:schemas.User = Depends(oauth2.get_current_user)
    return tag.delete(id,db)


