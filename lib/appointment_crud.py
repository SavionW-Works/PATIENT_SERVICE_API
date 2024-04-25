from sqlalchemy.orm import Session

from . import db_models


def get_appointment(db: Session, appointment_id: int): # Updated function name and parameter
    return db.query(db_models.Appointment).filter(db_models.Appointment.id == appointment_id).first() # Updated model name and parameter

def get_appointments(db: Session, skip: int = 0, limit: int = 100): # Updated function name
    return db.query(db_models.Appointment).offset(skip).limit(limit).all() # Updated model name
