from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..controllers import payments as controller
from ..schemas import payments as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Payments'],
    prefix="/payments"
)

@router.post("/", response_model=schema.Payment)
def create_payment(payment_data: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create_payment(db=db, payment_data=payment_data)

@router.get("/", response_model=List[schema.Payment])
def get_all_payments(db: Session = Depends(get_db)):
    return controller.get_all_payments(db=db)

@router.get("/{payment_id}", response_model=schema.Payment)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    return controller.get_payment(db=db, payment_id=payment_id)

@router.put("/{payment_id}", response_model=schema.Payment)
def update_payment(payment_id: int, payment_data: schema.PaymentUpdate, db: Session = Depends(get_db)):
    return controller.update_payment(db=db, payment_id=payment_id, payment_data=payment_data)

@router.delete("/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    return controller.delete_payment(db=db, payment_id=payment_id)