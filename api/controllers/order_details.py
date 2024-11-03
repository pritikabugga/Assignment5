from sqlalchemy.orm import Session
from ..models.models import OrderDetail  # Ensure OrderDetail class is defined in models.py

def create(db: Session, order_detail_data):
    """Create a new order detail entry in the database."""
    new_order_detail = OrderDetail(**order_detail_data)
    db.add(new_order_detail)
    db.commit()
    return new_order_detail

def read_all(db: Session):
    """Retrieve all order detail entries."""
    return db.query(OrderDetail).all()

def read_one(db: Session, order_detail_id):
    """Retrieve a single order detail by its ID."""
    return db.query(OrderDetail).filter_by(id=order_detail_id).first()

def update(db: Session, order_detail_id, update_data):
    """Update a specific order detail entry."""
    order_detail = db.query(OrderDetail).filter_by(id=order_detail_id).first()
    if order_detail:
        for key, value in update_data.items():
            setattr(order_detail, key, value)
        db.commit()
    return order_detail

def delete(db: Session, order_detail_id):
    """Delete a specific order detail entry by ID."""
    order_detail = db.query(OrderDetail).filter_by(id=order_detail_id).first()
    if order_detail:
        db.delete(order_detail)
        db.commit()
    return order_detail
