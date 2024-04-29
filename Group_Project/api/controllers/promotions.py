from sqlalchemy.orm import Session
from datetime import datetime
from typing import List
from ..schemas import PromotionCreate, PromotionUpdate
from ..models import Promotion

def create_promotion(db: Session, promotion: PromotionCreate):
    db_promotion = Promotion(**promotion.dict())
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion

def get_promotions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Promotion).offset(skip).limit(limit).all()

def get_promotion(db: Session, promotion_id: int):
    return db.query(Promotion).filter(Promotion.id == promotion_id).first()

def update_promotion(db: Session, promotion_id: int, promotion: PromotionUpdate):
    db_promotion = db.query(Promotion).filter(Promotion.id == promotion_id).first()
    if db_promotion is None:
        return None
    for var, value in vars(promotion).items():
        if value is not None:
            setattr(db_promotion, var, value)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion

def delete_promotion(db: Session, promotion_id: int):
    db_promotion = db.query(Promotion).filter(Promotion.id == promotion_id).first()
    if db_promotion is None:
        return False
    db.delete(db_promotion)
    db.commit()
    return True
