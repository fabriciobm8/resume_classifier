from sqlalchemy import Column, Integer, String, Float
from database import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    class_label = Column(String, index=True)
    seniority_label = Column(String, index=True)
    prob_class = Column(Float)
    prob_seniority = Column(Float)