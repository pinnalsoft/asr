from sqlalchemy import Boolean, Column, Integer, String, Text, PrimaryKeyConstraint
from sqlalchemy.dialects.mysql import BIT

from ..database import Base


class EleosDriverCredentials(Base):
    __tablename__ = "EleosDriverCredentials"

    DriverID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(200))
    Username = Column(String(100), unique=True, index=True)
    Password = Column(String(255))
    GeotabUsername = Column(String(100))
    GeotabPasswordStatus = Column(String(50))


class EleosDriverNotifications(Base):
    __tablename__ = "EleosDriverNotifications"
    __table_args__ = (
        PrimaryKeyConstraint("DriverID", "Username", "MessageBody"),
    )

    DriverID = Column(Integer)
    Username = Column(String(100))
    MessageBody = Column(Text)
    Contact = Column(String(100))
    Sound = Column(String(100))

