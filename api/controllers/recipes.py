from sqlalchemy.orm import Session
from ..models.models import Recipe  # Ensure Recipe class is defined in models.py

def create(db: Session, recipe_data):
    """Create a new recipe entry in the database."""
    new_recipe = Recipe(**recipe_data)
    db.add(new_recipe)
    db.commit()
    return new_recipe

def read_all(db: Session):
    """Retrieve all recipe entries."""
    return db.query(Recipe).all()

def read_one(db: Session, recipe_id):
    """Retrieve a single recipe by its ID."""
    return db.query(Recipe).filter_by(id=recipe_id).first()

def update(db: Session, recipe_id, update_data):
    """Update a specific recipe entry."""
    recipe = db.query(Recipe).filter_by(id=recipe_id).first()
    if recipe:
        for key, value in update_data.items():
            setattr(recipe, key, value)
        db.commit()
    return recipe

def delete(db: Session, recipe_id):
    """Delete a specific recipe entry by ID."""
    recipe = db.query(Recipe).filter_by(id=recipe_id).first()
    if recipe:
        db.delete(recipe)
        db.commit()
    return recipe
