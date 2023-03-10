from sqlalchemy import Column, Integer, String, DateTime, Numeric, SmallInteger

from fakenamesservice.database import Base

class Fakenames(Base):
    __tablename__ = 'fakenames'
    __table_args__ = {'extend_existing': True}
    
    number = Column(Integer, primary_key=True)
    gender = Column(String(6))
    nameset = Column(String(25))
    title = Column(String(6))
    givenname = Column(String(20))
    middleinitial = Column(String(1))
    surname = Column(String(23))
    streetaddress = Column(String(100))
    city = Column(String(100))
    state = Column(String(22))
    statefull = Column(String(100))
    zipcode = Column(String(15))
    country = Column(String(2))
    countryfull = Column(String(100))
    emailaddress = Column(String(100))
    username = Column(String(25))
    password = Column(String(25))
    browseruseragent = Column(String(255))
    telephonenumber = Column(String(25))
    telephonecountrycode = Column(Integer)
    mothersmaiden = Column(String(23))
    birthday = Column(DateTime)
    age = Column(Integer)
    tropicalzodiac = Column(String(11))
    cctype = Column(String(10))
    ccnumber = Column(String(16))
    cvv2 = Column(Numeric(3))
    ccexpires = Column(String(10))
    nationalid = Column(String(20))
    ups = Column(String(24))
    westernunionmtcn = Column(String(10))
    moneygrammtcn = Column(String(8))
    color = Column(String(6))
    occupation = Column(String(70))
    company = Column(String(70))
    vehicle = Column(String(255))
    domain = Column(String(70))
    bloodtype = Column(String(3))
    pounds = Column(Numeric(5, 1))
    kilograms = Column(Numeric(5, 1))
    feetinches = Column(String(6))
    centimeters = Column(SmallInteger)
    guid = Column(String(36))
    latitude = Column(Numeric(10, 8))
    longitude = Column(Numeric(11, 8))