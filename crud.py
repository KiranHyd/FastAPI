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
    db_account = models.Account(**account.dict(), ownerId=user_id)
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
            state_andhra.disabled = False
            

            state_arunachal = models.StateOrProvince()
            state_arunachal.stateOrProvince = 'Arunachal Pradesh'
            state_arunachal.countryId = country_india_id
            state_arunachal.disabled = False

            state_assam = models.StateOrProvince()
            state_assam.stateOrProvince = 'Assam'
            state_assam.countryId = country_india_id
            state_assam.disabled = False

            state_bihar = models.StateOrProvince()
            state_bihar.stateOrProvince = 'Bihar'
            state_bihar.countryId = country_india_id
            state_bihar.disabled = False

            state_chhattisgarh = models.StateOrProvince()
            state_chhattisgarh.stateOrProvince = 'Chhattisgarh'
            state_chhattisgarh.countryId = country_india_id
            state_chhattisgarh.disabled = False

            state_goa = models.StateOrProvince()
            state_goa.stateOrProvince = 'Goa'
            state_goa.countryId = country_india_id
            state_goa.disabled = False

            state_gujarat = models.StateOrProvince()
            state_gujarat.stateOrProvince = 'Gujarat'
            state_gujarat.countryId = country_india_id
            state_gujarat.disabled = False

            state_haryana = models.StateOrProvince()
            state_haryana.stateOrProvince = 'Haryana'
            state_haryana.countryId = country_india_id
            state_haryana.disabled = False

            state_himachal = models.StateOrProvince()
            state_himachal.stateOrProvince = 'Himachal Pradesh'
            state_himachal.countryId = country_india_id
            state_himachal.disabled = False

            state_jharkhand = models.StateOrProvince()
            state_jharkhand.stateOrProvince = 'Jharkhand'
            state_jharkhand.countryId = country_india_id
            state_jharkhand.disabled = False

            state_karnataka = models.StateOrProvince()
            state_karnataka.stateOrProvince = 'Karnataka'
            state_karnataka.countryId = country_india_id
            state_karnataka.disabled = False

            state_kerala = models.StateOrProvince()
            state_kerala.stateOrProvince = 'Kerala'
            state_kerala.countryId = country_india_id
            state_kerala.disabled = False

            state_madhya_pradesh = models.StateOrProvince()
            state_madhya_pradesh.stateOrProvince = 'Madhya Pradesh'
            state_madhya_pradesh.countryId = country_india_id
            state_madhya_pradesh.disabled = False

            state_maharashtra = models.StateOrProvince()
            state_maharashtra.stateOrProvince = 'Maharashtra'
            state_maharashtra.countryId = country_india_id
            state_maharashtra.disabled = False

            state_manipur = models.StateOrProvince()
            state_manipur.stateOrProvince = 'Manipur'
            state_manipur.countryId = country_india_id
            state_manipur.disabled = False

            state_meghalaya = models.StateOrProvince()
            state_meghalaya.stateOrProvince = 'Meghalaya'
            state_meghalaya.countryId = country_india_id
            state_meghalaya.disabled = False

            state_mizoram = models.StateOrProvince()
            state_mizoram.stateOrProvince = 'Mizoram'
            state_mizoram.countryId = country_india_id
            state_mizoram.disabled = False

            state_nagaland = models.StateOrProvince()
            state_nagaland.stateOrProvince = 'Nagaland'
            state_nagaland.countryId = country_india_id
            state_nagaland.disabled = False

            state_odisha = models.StateOrProvince()
            state_odisha.stateOrProvince = 'Odisha'
            state_odisha.countryId = country_india_id
            state_odisha.disabled = False

            state_punjab = models.StateOrProvince()
            state_punjab.stateOrProvince = 'Punjab'
            state_punjab.countryId = country_india_id
            state_punjab.disabled = False

            state_rajasthan = models.StateOrProvince()
            state_rajasthan.stateOrProvince = 'Rajasthan'
            state_rajasthan.countryId = country_india_id
            state_rajasthan.disabled = False

            state_sikkim = models.StateOrProvince()
            state_sikkim.stateOrProvince = 'Sikkim'
            state_sikkim.countryId = country_india_id
            state_sikkim.disabled = False

            state_tamilnadu = models.StateOrProvince()
            state_tamilnadu.stateOrProvince = 'Tamil Nadu'
            state_tamilnadu.countryId = country_india_id
            state_tamilnadu.disabled = False

            state_telangana = models.StateOrProvince()
            state_telangana.stateOrProvince = 'Telangana'
            state_telangana.countryId = country_india_id
            state_telangana.disabled = False

            state_tripura = models.StateOrProvince()
            state_tripura.stateOrProvince = 'Tripura'
            state_tripura.countryId = country_india_id
            state_tripura.disabled = False

            state_uttar_pradesh = models.StateOrProvince()
            state_uttar_pradesh.stateOrProvince = 'Uttar Pradesh'
            state_uttar_pradesh.countryId = country_india_id
            state_uttar_pradesh.disabled = False

            state_uttarakhand = models.StateOrProvince()
            state_uttarakhand.stateOrProvince = 'Uttarakhand'
            state_uttarakhand.countryId = country_india_id
            state_uttarakhand.disabled = False

            state_westbengal = models.StateOrProvince()
            state_westbengal.stateOrProvince = 'West Bengal'
            state_westbengal.countryId = country_india_id
            state_westbengal.disabled = False

            state_andaman_nicobar = models.StateOrProvince()
            state_andaman_nicobar.stateOrProvince = 'Andaman and Nicobar Islands'
            state_andaman_nicobar.countryId = country_india_id
            state_andaman_nicobar.disabled = False

            state_chandigarh = models.StateOrProvince()
            state_chandigarh.stateOrProvince = 'Chandigarh'
            state_chandigarh.countryId = country_india_id
            state_chandigarh.disabled = False

            state_dadra_and_nagar_haveli_and_daman_and_diu = models.StateOrProvince()
            state_dadra_and_nagar_haveli_and_daman_and_diu.stateOrProvince = 'Dadra and Nagar Haveli and Daman and Diu'
            state_dadra_and_nagar_haveli_and_daman_and_diu.countryId = country_india_id
            state_dadra_and_nagar_haveli_and_daman_and_diu.disabled = False

            state_delhi = models.StateOrProvince()
            state_delhi.stateOrProvince = 'Delhi'
            state_delhi.countryId = country_india_id
            state_delhi.disabled = False

            state_jammu_and_kashmir = models.StateOrProvince()
            state_jammu_and_kashmir.stateOrProvince = 'Jammu and Kashmir'
            state_jammu_and_kashmir.countryId = country_india_id
            state_jammu_and_kashmir.disabled = False

            state_ladakh = models.StateOrProvince()
            state_ladakh.stateOrProvince = 'Ladakh'
            state_ladakh.countryId = country_india_id
            state_ladakh.disabled = False

            state_lakshadweep = models.StateOrProvince()
            state_lakshadweep.stateOrProvince = 'Lakshadweep'
            state_lakshadweep.countryId = country_india_id
            state_lakshadweep.disabled = False

            state_puducherry = models.StateOrProvince()
            state_puducherry.stateOrProvince = 'Puducherry'
            state_puducherry.countryId = country_india_id
            state_puducherry.disabled = False

            db.add_all([state_andhra, 
                    state_arunachal,
                    state_assam,
                    state_bihar,
                    state_chhattisgarh,
                    state_goa,
                    state_gujarat,
                    state_haryana,
                    state_himachal,
                    state_jharkhand,
                    state_karnataka,
                    state_kerala,
                    state_madhya_pradesh,
                    state_maharashtra,
                    state_manipur,
                    state_meghalaya,
                    state_mizoram,
                    state_nagaland,
                    state_odisha,
                    state_punjab,
                    state_rajasthan,
                    state_sikkim,
                    state_tamilnadu,
                    state_telangana,
                    state_tripura,
                    state_uttar_pradesh,
                    state_uttarakhand,
                    state_westbengal,
                    state_andaman_nicobar,
                    state_chandigarh,
                    state_dadra_and_nagar_haveli_and_daman_and_diu,
                    state_delhi,
                    state_jammu_and_kashmir,
                    state_ladakh,
                    state_lakshadweep,
                    state_puducherry])
    db.commit()
    
    gender_count = db.query(func.count(models.Gender.genderId)).scalar()
    if gender_count == 0:
        gender_female = models.Gender()
        gender_female.gender = 'Female'
        gender_female.disabled = False

        gender_male = models.Gender()
        gender_male.gender = 'Male'
        gender_male.disabled = False

        gender_other = models.Gender()
        gender_other.gender = 'Other'
        gender_other.disabled = False

        db.add_all([gender_female, gender_male, gender_other])
        db.commit()

    maritalStatus_count = db.query(func.count(models.MaritalStatus.maritalStatusId)).scalar()
    if maritalStatus_count == 0:
        maritalStatus_divorced = models.MaritalStatus()
        maritalStatus_divorced.maritalStatus = 'Divorced'
        maritalStatus_divorced.disabled = False

        maritalStatus_married = models.MaritalStatus()
        maritalStatus_married.maritalStatus = 'Married'
        maritalStatus_married.disabled = False

        maritalStatus_unmarried = models.MaritalStatus()
        maritalStatus_unmarried.maritalStatus = 'Unmarried'
        maritalStatus_unmarried.disabled = False

        maritalStatus_widowed = models.MaritalStatus()
        maritalStatus_widowed.maritalStatus = 'Widowed'
        maritalStatus_widowed.disabled = False

        db.add_all([maritalStatus_divorced, maritalStatus_married, maritalStatus_unmarried, maritalStatus_widowed])
        db.commit()

    professionType_count = db.query(func.count(models.ProfessionType.professionTypeId)).scalar()
    if professionType_count == 0:
        
        professionType_none = models.ProfessionType()
        professionType_none.professionType = 'None'
        professionType_none.disabled = False

        professionType_business = models.ProfessionType()
        professionType_business.professionType = 'Business'
        professionType_business.disabled = False

        professionType_daily_worker = models.ProfessionType()
        professionType_daily_worker.professionType = 'Daily Worker'
        professionType_daily_worker.disabled = False

        professionType_farmer = models.ProfessionType()
        professionType_farmer.professionType = 'Farmer'
        professionType_farmer.disabled = False

        professionType_government_employee = models.ProfessionType()
        professionType_government_employee.professionType = 'Government Employee'
        professionType_government_employee.disabled = False

        professionType_private_employee = models.ProfessionType()
        professionType_private_employee.professionType = 'Private Employee'
        professionType_private_employee.disabled = False
     
        db.add_all([professionType_none,
                    professionType_business, 
                    professionType_daily_worker,
                    professionType_farmer,
                    professionType_government_employee,
                    professionType_private_employee 
                    ])
        db.commit()

    accountType_count = db.query(func.count(models.AccountType.accountTypeId)).scalar()
    if accountType_count == 0:
        accountType_secured_loan = models.AccountType()
        accountType_secured_loan.accountType = 'Secured Loan'
        accountType_secured_loan.disabled = False

        accountType_unsecured_loan = models.AccountType()
        accountType_unsecured_loan.accountType = 'Unsecured Loan'
        accountType_unsecured_loan.disabled = False

        db.add_all([accountType_secured_loan, accountType_unsecured_loan])
        db.commit()





