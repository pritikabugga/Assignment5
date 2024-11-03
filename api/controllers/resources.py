from sqlalchemy.orm import Session
from ..models.models import Resource  # Ensure Resource class is defined in models.py

def create(db: Session, resource_data):
    """Create a new resource entry in the database."""
    new_resource = Resource(**resource_data)
    db.add(new_resource)
    db.commit()
    return new_resource

def read_all(db: Session):
    """Retrieve all resource entries."""
    return db.query(Resource).all()

def read_one(db: Session, resource_id):
    """Retrieve a single resource by its ID."""
    return db.query(Resource).filter_by(id=resource_id).first()

def update(db: Session, resource_id, update_data):
    """Update a specific resource entry."""
    resource = db.query(Resource).filter_by(id=resource_id).first()
    if resource:
        for key, value in update_data.items():
            setattr(resource, key, value)
        db.commit()
    return resource

def delete(db: Session, resource_id):
    """Delete a specific resource entry by ID."""
    resource = db.query(Resource).filter_by(id=resource_id).first()
    if resource:
        db.delete(resource)
        db.commit()
    return resource
