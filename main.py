from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi import Request
import crud, models
import random

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# serve /static/image.jpg
app.mount("/static", StaticFiles(directory="static"), name="static")

# get a db session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/")
def root():
    return {"God's in His heaven": "all's right with the world"}
        
@app.get("/initdb")
def init_db():
    models.Base.metadata.create_all(bind=engine)
    return {"status": "tables created"}


@app.get("/register")
def register(query: str, db: Session = Depends(get_db)):
    crud.register_query(db, query)
    return {"status": "registered"}

@app.get("/getImage")
def get_image(query: str, request: Request, db: Session = Depends(get_db)):
    forwarded_for = request.headers.get("x-forwarded-for")
    ip = forwarded_for.split(",")[0].strip() if forwarded_for else request.client.host

    request_metadata = {
        "ip": ip,
        "user_agent": request.headers.get("user-agent"),
        "referer": request.headers.get("referer"),
        "accept": request.headers.get("accept"),
        "fly_region": request.headers.get("fly-region")
    }
    
    crud.register_query(db, query)
    crud.add_timestamp(db, query, request_metadata)
    
    timestamps = crud.get_timestamps(db, query)
    n = len(timestamps)
    selected_image = "static/image.jpeg"
    if n%5==0:
        selected_image = random.choice(["static/sahaqueil.jpg", "static/sahaqueil_.jpg"])
    return FileResponse(selected_image, media_type="image/jpeg")

@app.get("/getData")
def get_data(query: str, db: Session = Depends(get_db)):
    events = crud.get_timestamps(db, query)
    return {
        "query": query,
        "events": events
    }



@app.get("/clearData")
def clear_data(query: str, db: Session = Depends(get_db)):
    success = crud.clear_data(db, query)
    return {"status": "cleared" if success else "not found"}
