from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import payment as model
from sqlalchemy.exc import SQLAlchemyError


def handle_sqlalchemy_error(e: SQLAlchemyError):
    error = str(e)
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def create_or_update(db: Session, item_id=None, request=None):
    try:
        if item_id is None:
            new_item = model.Payment(
                payment_type=request.payment_type,
                payment_information=request.payment_information,
                transaction_status=request.transaction_status
            )
            db.add(new_item)
        else:
            item = db.query(model.Payment).filter(model.Payment.id == item_id).first()
            if not item:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment ID not found!")
            update_data = request.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(item, key, value)
        db.commit()
        db.refresh(new_item)
        return new_item if item_id is None else item
    except SQLAlchemyError as e:
        handle_sqlalchemy_error(e)


def read_all(db: Session):
    try:
        result = db.query(model.Payment).all()
        return result
    except SQLAlchemyError as e:
        handle_sqlalchemy_error(e)


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Payment).filter(model.Payment.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment ID not found!")
        return item
    except SQLAlchemyError as e:
        handle_sqlalchemy_error(e)


def delete(db: Session, item_id):
    try:
        item = db.query(model.Payment).filter(model.Payment.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment ID not found!")
        db.delete(item)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        handle_sqlalchemy_error(e)