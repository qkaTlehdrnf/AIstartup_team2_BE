from fastapi import status, HTTPException
from sqlalchemy.orm import Session 
from .. import schemas, models
from ..hashing import Hash



def assert_exist(picture):
    if not picture.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"picture already deleted")
    return True






###111
def read_all_pictures_by_blog_id(blog_id: int, db: Session):
    picture = db.query(models.Picture).filter(models.Picture.blog_id == blog_id).all()
    return picture






###222
def read_picture_by_picture_id(id: int, db: Session):
    picture = db.query(models.Picture).filter(models.Picture.id == id)
    assert_exist(picture)
    return picture.first()





###333
def create(request, db):
    new_picture = models.Picture(
        blog_id = request.blog_id, url=request.url)
    db.add(new_picture)
    db.commit()
    db.refresh(new_picture)
    return new_picture


###444
def delete(id: int, db: Session):    
    picture = db.query(models.Picture).filter(models.Picture.id == id)
    assert_exist(picture)
    picture.delete(synchronize_session=False)
    db.commit()
    return {'picture deleted'}