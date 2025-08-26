from fastapi import APIRouter

router = APIRouter()

@router.get("/{session_id}")
def get_report(session_id: str):
    

    return {"message": f"Report generation for session {session_id} is ready."}
