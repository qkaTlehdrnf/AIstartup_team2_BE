from sqlalchemy.orm import Session
from .. import models, schemas, database
from fastapi import status, HTTPException






def assert_blogid(blog):##blog is query type
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog not found")
    return True




###111
def read_all_blogs_by_user_id(user_id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.user_id == user_id).all()
    return blog






###222
def read_blog_by_blog_id(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sorry, Blog might not be found.")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f"Blog with the id {id} is not available"}
    return blog

###333
def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(
        user_id=request.user_id, body=request.body, 
        pic=request.pic, comment=request.comment)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

###444
def update(id:int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    assert_blogid(blog, id)
    blog.update({'body': request.body, 'user_id': request.user_id, 'pic': request.pic})
    db.commit()
    return 'done'



###555
def delete(id:int, db):
    
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    assert_blogid(blog, id)

    blog.delete(synchronize_session=False)
    db.commit()
    return {'done'}
