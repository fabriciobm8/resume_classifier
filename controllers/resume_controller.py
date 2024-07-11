from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
from services import resume_service

router = APIRouter()

class ResumeResponse(BaseModel):
    id: int
    filename: str
    class_label: str
    seniority_label: str
    prob_class: str
    prob_seniority: str

    class Config:
        orm_mode = True

@router.post("/predict/", response_model=ResumeResponse)
async def predict(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if file.content_type != 'application/pdf':
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are supported.")
    try:
        prediction_result = resume_service.create_prediction(db, file)
        return prediction_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@router.get("/predict/{resume_id}", response_model=ResumeResponse)
async def read_predict(resume_id: int, db: Session = Depends(get_db)):
    return resume_service.get_resume(db, resume_id)

@router.get("/predict/", response_model=list[ResumeResponse])
async def read_predicts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return resume_service.get_resumes(db, skip, limit)

@router.put("/predict/{resume_id}", response_model=ResumeResponse)
async def update_predict(resume_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    if file.content_type != 'application/pdf':
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are supported.")
    try:
        return resume_service.update_resume(db, resume_id, file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@router.delete("/predict/{resume_id}")
async def delete_predict(resume_id: int, db: Session = Depends(get_db)):
    return resume_service.delete_resume(db, resume_id)