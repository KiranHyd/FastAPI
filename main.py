import uvicorn
from datetime import datetime, timedelta
from typing import List
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import database
import auth, crud, models, schemas
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect mobile number or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.mobile}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(auth.get_current_active_user)):
    return current_user


@app.get("/users/me/accounts/")
async def read_own_accounts(current_user: schemas.User = Depends(auth.get_current_active_user)):
    return [{"account_id": "Foo", "owner": current_user.mobile}]



@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_mobile(db, mobile=user.mobile)
    if db_user:
        raise HTTPException(status_code=400, detail="Mobile already registered")
    user.password = auth.get_password_hash(user.password)
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/accounts/", response_model=schemas.Account)
def create_account_for_user(
    user_id: int, account: schemas.AccountCreate, db: Session = Depends(database.get_db)
):
    return crud.create_user_account(db=db, account=account, user_id=user_id)


@app.get("/accounts/", response_model=List[schemas.Account])
def read_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    accounts = crud.get_accounts(db, skip=skip, limit=limit)
    return accounts



if __name__ == '__main__':
    uvicorn.run('main:app', server_header=False)
