from models.resume_model import Resume
from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session
from utils.pdf_processing import preprocess_pdf
from utils.ml_models import vector_class, model_xgboost_class, vector_seniority, model_xgboost_seniority
import mapping

def create_prediction(db: Session, file: UploadFile):
    text = preprocess_pdf(file)
    X_tfidf_class = vector_class.transform([text])
    pred_class = model_xgboost_class.predict(X_tfidf_class)
    prob_class = model_xgboost_class.predict_proba(X_tfidf_class)[0]

    X_tfidf_seniority = vector_seniority.transform([text])
    pred_seniority = model_xgboost_seniority.predict(X_tfidf_seniority)
    prob_seniority = model_xgboost_seniority.predict_proba(X_tfidf_seniority)[0]

    indice_class = pred_class[0]
    class_texto = mapping.class_mapping[indice_class]

    indice_seniority = pred_seniority[0]
    seniority_texto = mapping.seniority_mapping[indice_seniority]

    original_filename = file.filename if file.filename.endswith(".pdf") else file.filename + ".pdf"
    filename = f"{original_filename[:-4]}_{class_texto}_{seniority_texto}.pdf"

    resume_data = {
        "filename": filename,
        "class_label": class_texto,
        "seniority_label": seniority_texto,
        "prob_class": prob_class[indice_class],
        "prob_seniority": prob_seniority[indice_seniority]
    }

    db_resume = Resume(**resume_data)
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)
    return format_resume_response(db_resume)

def get_resume(db: Session, resume_id: int):
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if resume is None:
        raise HTTPException(status_code=404, detail="Resume not found")
    return format_resume_response(resume)

def get_resumes(db: Session, skip: int = 0, limit: int = 10):
    resumes = db.query(Resume).offset(skip).limit(limit).all()
    return [format_resume_response(resume) for resume in resumes]

def update_resume(db: Session, resume_id: int, file: UploadFile):
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if resume is None:
        raise HTTPException(status_code=404, detail="Resume not found")

    text = preprocess_pdf(file)
    X_tfidf_class = vector_class.transform([text])
    pred_class = model_xgboost_class.predict(X_tfidf_class)
    prob_class = model_xgboost_class.predict_proba(X_tfidf_class)[0]

    X_tfidf_seniority = vector_seniority.transform([text])
    pred_seniority = model_xgboost_seniority.predict(X_tfidf_seniority)
    prob_seniority = model_xgboost_seniority.predict_proba(X_tfidf_seniority)[0]

    indice_class = pred_class[0]
    class_texto = mapping.class_mapping[indice_class]

    indice_seniority = pred_seniority[0]
    seniority_texto = mapping.seniority_mapping[indice_seniority]

    original_filename = file.filename if file.filename.endswith(".pdf") else file.filename + ".pdf"
    resume.filename = f"{original_filename[:-4]}_{class_texto}_{seniority_texto}.pdf"
    resume.class_label = class_texto
    resume.seniority_label = seniority_texto
    resume.prob_class = prob_class[indice_class]
    resume.prob_seniority = prob_seniority[indice_seniority]

    db.commit()
    db.refresh(resume)
    return format_resume_response(resume)

def delete_resume(db: Session, resume_id: int):
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if resume is None:
        raise HTTPException(status_code=404, detail="Resume not found")

    db.delete(resume)
    db.commit()
    return {"message": "Resume deleted successfully"}

def format_resume_response(resume: Resume):
    resume.prob_class = f"{resume.prob_class * 100:.2f}%"
    resume.prob_seniority = f"{resume.prob_seniority * 100:.2f}%"
    return resume