from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Numeric

Base = declarative_base()

class Application(Base):
    __tablename__ = 'application'

    IdProject = Column(Integer, primary_key=True, nullable=False)
    IdCompany = Column(Integer, nullable=True)
    IdManager = Column(Integer, nullable=True)
    IdSupportProgram = Column(Integer, nullable=True)
    LoanAmount = Column(Numeric, nullable=True)
    IdIndustry = Column(Integer, nullable=True)
    IdStatus = Column(Integer, nullable=True)
    IdSubindustry = Column(Integer, nullable=True)
    IdRegion = Column(Integer, nullable=True)
    ApplicationNumber = Column(String, nullable=True)
    ProjectName = Column(String, nullable=True)
    Locality = Column(String, nullable=True)
    LoanAgreementDate = Column(DateTime, nullable=True)
    IdBudget = Column(Integer, nullable=True)
    LoanAgreementPayement = Column(DateTime, nullable=True)
    IdRegionalFund = Column(Integer, nullable=True)

class ApplicationStatusHistory(Base):
    __tablename__ = 'ApllicationStatusHistory'

    Id = Column(Integer, primary_key=True)
    IdProject = Column(Integer, nullable=True)
    IdCurrentStatus = Column(Integer, nullable=True)
    IdPreviousStatus = Column(Integer, nullable=True)
    StatusBeginDate = Column(DateTime, nullable=True)
    StatusEndDate = Column(DateTime, nullable=True)
    
    def __repr__(self):
        return f'Id: {self.Id}\nProject Id: {self.IdProject}\nCurrent Status: {self.IdCurrentStatus}\nPrevious Status: {self.IdPreviousStatus}\nStart Date: {self.StatusBeginDate}\nEnd Date: {self.StatusEndDate}'

#test = ApplicationStatusHistory(42, 102, 12, 11, '01-01-2019', '31-01-2019')
#print(test)

class Industry(Base):
    __tablename__ = 'Industries'

    Id = Column(Integer, primary_key=True)
    IndustryName = Column(String, nullable=True)
    IdReportIndustry = Column(String, nullable=True)

class ReportIndustry(Base):
    __tablename__ = 'ReportIndustries'

    Id = Column(Integer, primary_key=True)
    ReportIndustryName = Column(String, nullable=True)


class Status(Base):
    __tablename__ = 'Statuses'

    Id = Column(Integer, primary_key=True)
    StatusName = Column(String, nullable=True)
