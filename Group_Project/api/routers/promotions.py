from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..controllers import promotions as controller
from ..schemas.promotions import Promotion, PromotionCreate, PromotionUpdate
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Promotions'],
    prefix="/promotions"
)

@router.post("/promotions/", response_model=Promotion)
def create_promotion_route(promotion: PromotionCreate, db: Session = Depends(get_db)):
    return controller.create_promotion(db, promotion)

@router.get("/promotions/", response_model=List[Promotion])
def read_promotions_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return controller.get_promotions(db, skip, limit)

@router.get("/promotions/{promotion_id}", response_model=Promotion)
def read_promotion_route(promotion_id: int, db: Session = Depends(get_db)):
    db_promotion = controller.get_promotion(db, promotion_id)
    if db_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return db_promotion

@router.put("/promotions/{promotion_id}", response_model=Promotion)
def update_promotion_route(promotion_id: int, promotion: PromotionUpdate, db: Session = Depends(get_db)):
    db_promotion = controller.update_promotion(db, promotion_id, promotion)
    if db_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return db_promotion

@router.delete("/promotions/{promotion_id}")
def delete_promotion_route(promotion_id: int, db: Session = Depends(get_db)):
    success = controller.delete_promotion(db, promotion_id)
    if not success:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return {"message": "Promotion deleted successfully"}
