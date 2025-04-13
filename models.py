from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, JSON
import pytz
import datetime

india = pytz.timezone("Asia/Kolkata")


class QueryEntry(Base):
    __tablename__ = "queries"
    id = Column(Integer, primary_key=True, index=True)
    query = Column(String, index=True)

    timestamps = relationship("TimestampEntry", back_populates="owner")

class TimestampEntry(Base):
    __tablename__ = "timestamps"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(india))
    query_id = Column(Integer, ForeignKey("queries.id"))
    request_metadata = Column(JSON, nullable=True)

    owner = relationship("QueryEntry", back_populates="timestamps")
