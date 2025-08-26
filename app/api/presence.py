from fastapi import APIRouter, File, UploadFile

router = APIRouter()

@router.post("/check")
async def check_presence(image: UploadFile = File(...)):
    """
    Placeholder for presence detection. 
    This will eventually send the frame to the Gemini API.
    """
    return {"filename": image.filename, "status": "User is present (simulated)."}
