from sqlalchemy import Boolean, Column, Integer, String, Text

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

    DriverID = Column(Integer, primary_key=True)
    Username = Column(String(100), primary_key=True)
    MessageBody = Column(Text)
    Contact = Column(String(100))
    Sound = Column(String(100))
