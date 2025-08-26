from fastapi import APIRouter, File, UploadFile

router = APIRouter()

@router.post("/check")
async def check_presence(image: UploadFile = File(...)):
    
    
    
    return {"filename": image.filename, "status": "User is present (simulated)."}
