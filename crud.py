from sqlalchemy.orm import Session
from models import QueryEntry, TimestampEntry

def register_query(db: Session, query: str):
    db_query = db.query(QueryEntry).filter(QueryEntry.query == query).first()
    if not db_query:
        db_query = QueryEntry(query=query)
        db.add(db_query)
        db.commit()
        db.refresh(db_query)
    return db_query

def add_timestamp(db: Session, query: str):
    db_query = register_query(db, query)
    new_ts = TimestampEntry(query_id=db_query.id)
    db.add(new_ts)
    db.commit()

def get_timestamps(db: Session, query: str):
    db_query = db.query(QueryEntry).filter(QueryEntry.query == query).first()
    if db_query:
        return [ts.timestamp for ts in db_query.timestamps]
    return []
