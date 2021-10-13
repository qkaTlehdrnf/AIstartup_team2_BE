from .database import Base
from sqlalchemy import Column, Integer,String,ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"###Simply, delete db and remake it can be answer. I don't know why

    id=Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blog = relationship("Blog",back_populates="user")
    comment = relationship("Comment",back_populates="user")

class Blog(Base):
    __tablename__ = 'blog'

    id=Column(Integer, primary_key=True, index=True)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    pic = Column(String)##nosql url for blog picture
    comment = Column(String)###nosql url for blog picture
    pic = relationship("Picture",back_populates="blog")
    comment = relationship("Comment",back_populates="blog")
    user  = relationship("User",back_populates="blog")

class Comment(Base):
    __tablename__ = "comment"

    id=Column(Integer, primary_key=True, index=True)
    body=Column(String)

    user_id = Column(Integer, ForeignKey('user.id'))
    blog_id = Column(Integer, ForeignKey('blog.id'))
    user = relationship("User",back_populates="comment")
    blog = relationship("Blog",back_populates="comment")

class Picture(Base):
    __tablename__ = "pic"

    id=Column(Integer, primary_key=True, index=True)
    url = Column(String)
    blog_id = Column(Integer, ForeignKey('blog.id'))
    blog=relationship("Blog",back_populates="pic")
    

    