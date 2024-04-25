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
from lib import appointment_crud
from lib import nurse_crud
from lib import patient_crud 
from lib import physician_crud 
from lib import prescription_crud  

from lib import response_models
from lib.database_connection import SessionLocal



app = FastAPI() 

origins = [
    "http://localhost:3000",
    "http://localhost:8000",    
    "https://localhost:3000",
    "https://localhost:8000",  
    "localhost:8000", 
    "localhost:3000",

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

@app.get("/hospital/", response_model=List[response_models.Hospital])
def get_hospitals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    hospitals = hospital_crud.get_hospitals(db, skip=skip, limit=limit)
    return hospitals 

@app.get("/patients/", response_model=List[response_models.Patient])
def get_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patients = patient_crud.get_patients(db, skip=skip, limit=limit)
    return patients

@app.get("/patients/{id}", response_model=response_models.Patient)
def get_patients_by_id(id: int, db: Session = Depends(get_db)):
    patient = patient_crud.get_patient(db, id)
    return patient

@app.get("/physician/", response_model=List[response_models.Physician])
def get_physicians(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    physicians = physician_crud.get_physicians(db, skip=skip, limit=limit)
    return physicians  

@app.get("/prescription/", response_model=List[response_models.Prescription])
def get_prescriptions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    prescriptions = prescription_crud.get_prescriptions(db, skip=skip, limit=limit)
    return prescriptions   


@app.get("/nurse/", response_model=List[response_models.Nurse])
def get_nurses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    nurses = nurse_crud.get_nurses(db, skip=skip, limit=limit)
    return nurses 

@app.get("/appointment/", response_model=List[response_models.Appointment]) # Updated route
def get_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)): # Updated function name
    appointments = appointment_crud.get_appointments(db, skip=skip, limit=limit) # Updated function call
    return appointments







#CORS allowed origins

# python -m uvicorn main:app --reload
