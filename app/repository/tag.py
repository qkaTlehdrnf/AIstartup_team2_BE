from fastapi import status, HTTPException
from sqlalchemy.orm import Session 
from .. import schemas, models
from ..hashing import Hash



def assert_exist(tag):
    if not tag.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"tag already deleted")
    return True






###111
def read_all_tags_by_blog_id(blog_id: int, db: Session):
    tag = db.query(models.Tag).filter(models.Tag.blog_id == blog_id).all()
    return tag






###222
def read_tag_by_tag_id(id: int, db: Session):
    tag = db.query(models.Tag).filter(models.Tag.id == id)
    assert_exist(tag)
    return tag.first()





###333
def read_all_blogs_by_tag_id(tag_id: int, db: Session):
    tag = db.query(models.Tag).filter(models.Tag.blog_id == tag_id).all()
    return tag






###444
def create(request, db):
    new_tag = models.Tag(
        blog_id = request.blog_id, url=request.url)
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag


###555
def delete(id: int, db: Session):    
    tag = db.query(models.Tag).filter(models.Tag.id == id)
    assert_exist(tag)
    tag.delete(synchronize_session=False)
    db.commit()
    return {'tag deleted'}