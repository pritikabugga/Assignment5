from sqlalchemy.orm import Session
from ..models.models import Sandwich  # Ensure Sandwich class is defined in models.py

def create(db: Session, sandwich_data):
    """Create a new sandwich entry in the database."""
    new_sandwich = Sandwich(**sandwich_data)
    db.add(new_sandwich)
    db.commit()
    return new_sandwich

def read_all(db: Session):
    """Retrieve all sandwich entries."""
    return db.query(Sandwich).all()

def read_one(db: Session, sandwich_id):
    """Retrieve a single sandwich by its ID."""
    return db.query(Sandwich).filter_by(id=sandwich_id).first()

def update(db: Session, sandwich_id, update_data):
    """Update a specific sandwich entry."""
    sandwich = db.query(Sandwich).filter_by(id=sandwich_id).first()
    if sandwich:
        for key, value in update_data.items():
            setattr(sandwich, key, value)
        db.commit()
    return sandwich

def delete(db: Session, sandwich_id):
    """Delete a specific sandwich entry by ID."""
    sandwich = db.query(Sandwich).filter_by(id=sandwich_id).first()
    if sandwich:
        db.delete(sandwich)
        db.commit()
    return sandwich
