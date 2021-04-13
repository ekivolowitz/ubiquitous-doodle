from star_tides.services.sql.database import db
from sqlalchemy import Column, BLOB


class UserModel(db.Model):
    __tablename__ = 'users'
    id = Column(db.Integer, primary_key=True)
    first_name = Column(db.String, nullable=False)
    last_name = Column(db.String, nullable=False)
    email = Column(db.String, nullable=False)
    password_hash = Column(BLOB, nullable=True)