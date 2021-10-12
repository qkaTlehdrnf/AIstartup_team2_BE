from sqlalchemy.orm import Session
from .. import models, schemas, database
from fastapi import APIRouter, Depends, status, HTTPException


def assert_blogid(blog, id):
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found")
    return True

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destory(id:int, db:Session):
    
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    assert_blogid(blog, id)

    blog.delete(synchronize_session=False)
    db.commit()
    return {'done'}

def update(id:int, request: schemas.Blog, db: Session):
    

    blog = db.query(models.Blog).filter(models.Blog.id == id)

    assert_blogid(blog, id)

    blog.update({'title': request.title, 'body': request.body})
    # I don't know why I have to write in this way.
    # Tutorial said it is enought to write blog.update(request)
    db.commit()

    return 'done'

def show(id: int, db: Session):
    
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f"Blog with the id {id} is not available"}
    return blog