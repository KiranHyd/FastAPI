from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Country(Base):
    __tablename__ = "countries"

    countryId = Column(Integer, primary_key=True, index=True)
    country = Column(String, unique=True, index=True)
    disabled = Column(Boolean, default=False)

    stateOrProvinces = relationship("StateOrProvince", back_populates="country")
    
class StateOrProvince(Base):
    __tablename__ = "stateOrProvinces"

    stateOrProvinceId = Column(Integer, primary_key=True, index=True)
    stateOrProvince = Column(String, unique=True, index=True)
    countryId = Column(Integer, ForeignKey("countries.countryId"))
    disabled = Column(Boolean, default=False)

    country = relationship("Country", back_populates="stateOrProvinces")

    users = relationship("User", back_populates="stateOrProvince")

class Gender(Base):
    __tablename__ = "genders"

    genderId = Column(Integer, primary_key=True, index=True)
    gender = Column(String, unique=True, index=True)
    disabled = Column(Boolean, default=False)

    users = relationship("User", back_populates="gender")
    
class MaritalStatus(Base):
    __tablename__ = "maritalStatuses"

    maritalStatusId = Column(Integer, primary_key=True, index=True)
    maritalStatus = Column(String, unique=True, index=True)
    disabled = Column(Boolean, default=False)

    users = relationship("User", back_populates="maritalStatus")

class ProfessionType(Base):
    __tablename__ = "professionTypes"

    professionTypeId = Column(Integer, primary_key=True, index=True)
    professionType = Column(String, unique=True, index=True)
    description = Column(String)
    disabled = Column(Boolean, default=False)

    users = relationship("User", back_populates="profession")
    
class AccountType(Base):
    __tablename__ = "accountTypes"

    accountTypeId = Column(Integer, primary_key=True, index=True)
    accountType = Column(String, unique=True, index=True)
    description = Column(String)
    disabled = Column(Boolean, default=False)

    accounts = relationship("Account", back_populates="accountType")

class AccountStatus(Base):
    __tablename__ = "accountStatuses"

    accountStatusId = Column(Integer, primary_key=True, index=True)
    accountStatus = Column(String, unique=True, index=True)
    description = Column(String)
    disabled = Column(Boolean, default=False)

    accounts = relationship("Account", back_populates="accountStatus")

class ActivityType(Base):
    __tablename__ = "activityTypes"

    activityTypeId = Column(Integer, primary_key=True, index=True)
    activityType = Column(String, unique=True, index=True)
    description = Column(String)

class ErrorType(Base):
    __tablename__ = "errorTypes"

    errorTypeId = Column(Integer, primary_key=True, index=True)
    errorType = Column(String, unique=True, index=True)
    description = Column(String)

class User(Base):
    __tablename__ = "users"

    userId = Column(Integer, primary_key=True, index=True)
    firstName = Column(String)
    lastName = Column(String)
    adhaarNumber = Column(String, unique=True, index=True)
    panOrTinNumber = Column(String, unique=True, index=True)
    adhaarRegisteredMobileNumber = Column(String, unique=True, index=True)
    alternateMobileNumber = Column(String, unique=True, index=True)
    emailAddress = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    currentAddress = Column(String)
    permanentAddress = Column(String)
    fatherOrSpouseName = Column(String)
    annualIncome = Column(Float)
    adhaarVerified = Column(Boolean, default=False)
    professionAndIncomeVerified = Column(Boolean, default=False)
    dateOfBirthOrIncorporation = Column(Date)
    pinCode = Column(String)
    referredBy = Column(String, index=True)
    disabled = Column(Boolean, default=False)
    createdAt = Column(DateTime)
   
    genderId = Column(Integer, ForeignKey("genders.genderId"))
    professionTypeId = Column(Integer, ForeignKey("professionTypes.professionTypeId"))
    maritalStatusId = Column(Integer, ForeignKey("maritalStatuses.maritalStatusId"))
    
    stateOrProvinceId = Column(Integer, ForeignKey("stateOrProvinces.stateOrProvinceId"))

    gender = relationship("Gender", back_populates="users")
    profession = relationship("ProfessionType", back_populates="users")
    maritalStatus = relationship("MaritalStatus", back_populates="users")
    stateOrProvince = relationship("StateOrProvince", back_populates="users")
    
    ownerAccounts = relationship("Account", back_populates="owner")
    #agentAccounts = relationship("Account", back_populates="agent")
    transactions = relationship("Transaction", back_populates="transactionUser")
    activityLog = relationship("ActivityLog", back_populates="user")
    errorLog = relationship("ErrorLog", back_populates="user")
    

class Account(Base):
    __tablename__ = "accounts"

    accountId = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    rateOfInterest = Column(Float)
    balance = Column(Float)
    disabled = Column(Boolean, default=False)
    openedAt = Column(DateTime)
    modifiedAt = Column(DateTime)
    closedAt = Column(DateTime)
    ownerId = Column(Integer, ForeignKey("users.userId"))
    agentId = Column(Integer, index=True)
    accountTypeId = Column(Integer, ForeignKey("accountTypes.accountTypeId"))
    accountStatusId = Column(Integer, ForeignKey("accountStatuses.accountStatusId"))
    
    owner = relationship("User", back_populates="ownerAccounts")
    #agent = relationship("User", back_populates="agentAccounts")
    accountType = relationship("AccountType", back_populates="accounts")
    accountStatus = relationship("AccountStatus", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")

class Transaction(Base):
    __tablename__ = "transactions"
    transactionId = Column(Integer, primary_key=True, index=True)
    transactionAmount = Column(Float)
    balance = Column(Float)
    refOrChequeNo = Column(String)
    description = Column(String)
    transactionDateTime = Column(DateTime)
    accountId = Column(Integer, ForeignKey("accounts.accountId"))
    transactionById = Column(Integer, ForeignKey("users.userId"))

    account = relationship("Account", back_populates="transactions")
    transactionUser = relationship("User", back_populates="transactions")

class AppConfig(Base):
    __tablename__ = "appConfig"

    configId = Column(Integer, primary_key=True, index = True)
    configName = Column(String, unique=True)
    description = Column(String)
    configValue = Column(String)
    createdDateTime = Column(DateTime)
    updatedDateTime = Column(DateTime)
    createdById = Column(Integer, ForeignKey("users.userId"))
    updatedById = Column(Integer, ForeignKey("users.userId"))

    # createdByUser = relationship("User", back_populates="appConfig")
    # modifiedByUser = relationship("User", back_populates="appConfig")

class ActivityLog(Base):
    __tablename__ = "activityLog"
    
    activityId = Column(Integer, primary_key=True, index = True)
    description = Column(String)
    activityTimeStamp = Column(DateTime)
    urlOrModule = Column(String)
    activityTypeId = Column(Integer, ForeignKey("activityTypes.activityTypeId"))
    userId = Column(Integer, ForeignKey("users.userId"))
    
    user = relationship("User", back_populates="activityLog")

class ErrorLog(Base):
    __tablename__ = "errorLog"
    
    errorId = Column(Integer, primary_key=True, index = True)
    description = Column(String)
    errorTimeStamp = Column(DateTime)
    urlOrModule = Column(String)
    errorTypeId = Column(Integer, ForeignKey("errorTypes.errorTypeId"))
    userId = Column(Integer, ForeignKey("users.userId"))
    
    user = relationship("User", back_populates="errorLog")
