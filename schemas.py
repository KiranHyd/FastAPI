
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
    class Config:
        orm_mode = True

class StateOrProvinceBase(BaseModel):
    stateOrProvince: str

class StateOrProvince(CountryBase):
    stateOrProvinceId: int
    class Config:
        orm_mode = True

class AccountBase(BaseModel):
    name: str
    description: Optional[str] = None


class AccountCreate(AccountBase):
    pass


class Account(AccountBase):
    id: int
    owner_id: int

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


