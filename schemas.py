
from datetime import datetime
from typing import List, Optional
import pydantic
from pydantic import BaseModel
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class MobileMissingError(Exception):
    """Custom error that is raised when mobile no. is missing."""

    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)


class MobileFormatError(Exception):
    """Custom error that is raised when Mobile number doesn't have the right format."""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)

class CountryBase(BaseModel):
    country: str

class Country(CountryBase):
    countryId: int
    disabled: bool
    class Config:
        orm_mode = True

class StateOrProvinceBase(BaseModel):
    stateOrProvince: str

class StateOrProvince(StateOrProvinceBase):
    stateOrProvinceId: int
    disabled: bool
    class Config:
        orm_mode = True

class GenderBase(BaseModel):
    gender: str
    disabled: bool

class Gender(GenderBase):
    genderId: int
    class Config:
        orm_mode = True
class MaritalStatusBase(BaseModel):
    maritalStatus: str
    disabled: bool

class MaritalStatus(MaritalStatusBase):
    maritalStatusId: int
    class Config:
        orm_mode = True

class ProfessionTypeBase(BaseModel):
    professionType: str
    description: str
    disabled: bool

class ProfessionType(ProfessionTypeBase):
    professionTypeId: int
    class Config:
        orm_mode = True

class AccountTypeBase(BaseModel):
    accountType: str
    description: str
    disabled: bool

class AccountType(AccountTypeBase):
    accountTypeId: int
    class Config:
        orm_mode = True
       

class AccountStatusBase(BaseModel):
    accountStatus: str
    description: str
    disabled: bool

class AccountStatus(AccountStatusBase):
    accountStatusId: int
    class Config:
        orm_mode = True

class ActivityTypeBase(BaseModel):
    activityType: str
    description: str
class ActivityType(ActivityTypeBase):
    activityTypeId: int
    class Config:
        orm_mode = True

class ErrorTypeBase(BaseModel):
    errorType: str
    description: str
class ErrorType(ErrorTypeBase):
    errorTypeId: int
    class Config:
        orm_mode = True

class ActivityLogBase(BaseModel):
    description: str
    activityTimeStamp: datetime
    urlOrModule: str
    activityTypeId: str
    userId: int

class ActivityLogCreate(ActivityLogBase):
    pass

class ActivityLog(ActivityLogBase):
    activityId: int
    
class ErrorLogBase(BaseModel):
    description: str
    errorTimeStamp: datetime
    urlOrModule: str
    errorTypeId: str
    userId: int

class ErrorLogCreate(ErrorLogBase):
    pass

class ErrorLog(ErrorLogBase):
    errorId: int

class AppConfigBase(BaseModel):
    configName: str
    description: str
    configValue: str

class AppConfigCreate(AppConfigBase):
    pass

class AppConfig(AppConfigBase):
    configId: int
    createdDateTime: datetime
    updatedDateTime: datetime
    createdById: int
    updatedById: int
    disabled: bool
    class Config:
        orm_mode = True

class AccountBase(BaseModel):
    name: str
    description: Optional[str] = None
    rateOfInterest: float
    balance: float
    ownerId: int
    agentId: int
    accountTypeId: int
    AccountStatusId: int

class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    accountId: int
    disabled: bool
    openedAt: datetime
    modifiedAt: datetime
    closedAt: datetime
    class Config:
        orm_mode = True

class TransactionBase(BaseModel):
    transactionAmount: float
    balance: float
    refOrChequeNo: str
    description: str
    accountId: int


class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    transactionId: int
    transactionDateTime: datetime
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    adhaarRegisteredMobileNumber: str
    alternateMobileNumber: str
    firstName: str
    lastName: Optional[str]
    adhaarNumber: Optional[str]
    currentAddress: str
    permanentAddress: str
    fatherOrSpouseName: str
    annualIncome: float
    emailAddress: Optional[str]
    professionAndIncomeVerified: bool
    adhaarVerified: bool
    dateOfBirthOrIncorporation: datetime
    pinCode: str
    referredBy: str
    disabled: bool
    genderId: int
    professionTypeId: int
    maritalStatusId: int
    countryId: int
    stateOrProvinceId: int
    

    # @pydantic.root_validator(pre=True)
    # @classmethod
    # def checkMobileNumber(cls, values):
    #     """Make sure the mobile number is provided"""
    #     if "adhaarRegisteredMobileNumber" not in values:
    #         raise MobileMissingError(
    #             email=values["email"],
    #             message="User should have Mobile number",
    #         )
    #     return values


    @pydantic.validator("adhaarRegisteredMobileNumber")
    @classmethod
    def mobile_valid(cls, value) -> None:
        """Validator to check whether mobile is valid"""
        
        if not carrier._is_mobile(number_type(phonenumbers.parse(value))):
            raise MobileFormatError(value=value, message="Invalid mobile number.")

        return value

class UserCreate(UserBase):
    password: str


class User(UserBase):
    userId: int
    disabled: bool
    accounts: List[Account] = []

    class Config:
        orm_mode = True


