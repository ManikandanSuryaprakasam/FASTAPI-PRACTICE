"""SQLAlchemy ORM models for the application.

Defines two mapped classes used to create and query the database:

- dbUser:
  - __tablename__ = "users"
  - Columns: id (Integer, PK, indexed), username (String), email (String), password (String)
  - Relationship: items -> one-to-many relationship to dbArticle (back_populates="user")

- dbArticle:
  - __tablename__ = "articles"
  - Columns: id (Integer, PK, indexed), title (String), content (String), published (Boolean), user_id (Integer, FK -> users.id)
  - Relationship: user -> many-to-one relationship to dbUser (back_populates="items")

Both classes inherit from db.database.Base and are used by SQLAlchemy to create tables and perform ORM operations.
"""



from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from db.database import Base
from sqlalchemy.orm import relationship


class dbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship("dbArticle", back_populates="user")

class dbArticle(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("dbUser", back_populates="items")