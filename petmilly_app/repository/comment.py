from fastapi import status, HTTPException
from sqlalchemy.orm import Session 
from .. import schemas, models
from ..hashing import Hash



def assert_exist(comment):
    if not comment.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"comment already deleted")
    return True






###111
def read_all_comments_by_blog_id(id: int, db: Session):
    comment = db.query(models.Comment).filter(models.Comment.id == id).all()
    return comment






###222
def read_comment_by_comment_id(id: int, db: Session):
    comment = db.query(models.Comment).filter(models.Comment.id == id)
    assert_exist(comment)
    return comment.first()





###333
def create(request, db):
    new_comment = models.Comment(
        user_id=request.user_id, blog_id = request.blog_id, body=request.body)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


###444
def delete(id: int, db: Session):    
    comment = db.query(models.Comment).filter(models.Comment.id == id)
    assert_exist(comment)
    comment.delete(synchronize_session=False)
    db.commit()
    return {'comment deleted'}