from hashlib import new
from sqlalchemy import func
from sqlalchemy.orm import Session
import models, schemas, database

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_mobile(db: Session, mobile: str):
    return db.query(models.User).filter(models.User.adhaarRegisteredMobileNumber == mobile).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    #assuming hashed password is passed here
    db_user = models.User(adhaarRegisteredMobileNumber = user.adhaarRegisteredMobileNumber, email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_accounts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Account).offset(skip).limit(limit).all()


def create_user_account(db: Session, account: schemas.AccountCreate, user_id: int):
    db_account = models.Account(**account.dict(), owner_id=user_id)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

 
def initialize_database():
    db = database.SessionLocal()
    #countries = db.query(models.Country).all()
    countries_count = db.query(func.count(models.Country.countryId)).scalar()
    if countries_count == 0:
        country_india = models.Country()
        country_india.country = 'India'
        

        country_other = models.Country()
        country_other.country = 'Other'

        db.add_all([country_india, country_other])
        db.commit()

    
    states_count = db.query(func.count(models.StateOrProvince.stateOrProvinceId)).scalar()
    if states_count == 0:
        
        #countries = db.query(models.Country).all()
        country_india = db.query(models.Country).filter(func.lower(models.Country.country) == 'india').first()
        if country_india is not None:
            country_india_id = country_india.countryId
            state_andhra = models.StateOrProvince()
            state_andhra.stateOrProvince = 'Andhra Pradesh'
            state_andhra.countryId = country_india_id
            

            state_arunachal = models.StateOrProvince()
            state_arunachal.stateOrProvince = 'Arunachal Pradesh'
            state_arunachal.countryId = country_india_id

            state_assam = models.StateOrProvince()
            state_assam.stateOrProvince = 'Assam'
            state_assam.countryId = country_india_id

            db.add_all([state_andhra, 
                    state_arunachal,
                    state_assam])


    db.commit()
    # db.expire_all()



