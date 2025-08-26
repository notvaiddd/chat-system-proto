

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..models import models, schemas
from ..database import get_db


router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)

def create_session(db: Session = Depends(get_db)):
    

    return {"message": "Session creation endpoint is ready."}

@router.put("/{session_id}/end", status_code=status.HTTP_200_OK)
def end_session(session_id: str, db: Session = Depends(get_db)):
    
    return {"message": f"Session {session_id} ended."}
