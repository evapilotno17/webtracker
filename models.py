from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class QueryEntry(Base):
    __tablename__ = "queries"
    id = Column(Integer, primary_key=True, index=True)
    query = Column(String, index=True)

    timestamps = relationship("TimestampEntry", back_populates="owner")

class TimestampEntry(Base):
    __tablename__ = "timestamps"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    query_id = Column(Integer, ForeignKey("queries.id"))

    owner = relationship("QueryEntry", back_populates="timestamps")
