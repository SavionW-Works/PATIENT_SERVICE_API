#!/usr/bin/env python
""" This is the entrypoint to the Patient Service API.
"""

from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session



from lib import department_crud 
from lib import employee_crud 
from lib import hospital_crud  
from lib import insurance_crud 
from lib import medication_crud
from lib import patient_crud 
from lib import physician_crud 
from lib import prescription_crud  

from lib import response_models
from lib.database_connection import SessionLocal



app = FastAPI() 

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000/patients",  
    "https://localhost:3000/patients", 
    "localhost:3000"
] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
) 
# Dependency
def get_db():
    db = SessionLocal() 
    
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/patients/", response_model=List[response_models.Patient])
def get_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patients = patient_crud.get_patients(db, skip=skip, limit=limit)
    return patients


@app.get("/physician/", response_model=List[response_models.Physician])
def get_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    physicians = physician_crud.get_physicians(db, skip=skip, limit=limit)
    return physicians  

@app.get("/prescription/", response_model=List[response_models.Physician])
def get_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    physicians = physician_crud.get_physicians(db, skip=skip, limit=limit)
    return physicians 




#CORS allowed origins

# python -m uvicorn main:app --reload
