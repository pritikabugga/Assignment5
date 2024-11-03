from sqlalchemy.orm import Session
from ..models.models import Order

def create(db: Session, order_data):
    """Create a new order entry in the database."""
    new_order = Order(**order_data)
    db.add(new_order)
    db.commit()
    return new_order

def read_all(db: Session):
    """Retrieve all order entries."""
    return db.query(Order).all()

def read_one(db: Session, order_id):
    """Retrieve a single order by its ID."""
    return db.query(Order).filter_by(id=order_id).first()

def update(db: Session, order_id, update_data):
    """Update a specific order entry."""
    order = db.query(Order).filter_by(id=order_id).first()
    if order:
        for key, value in update_data.items():
            setattr(order, key, value)
        db.commit()
    return order

def delete(db: Session, order_id):
    """Delete a specific order entry by ID."""
    order = db.query(Order).filter_by(id=order_id).first()
    if order:
        db.delete(order)
        db.commit()
    return order
