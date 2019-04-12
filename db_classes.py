from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

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

class Status(Base):
    __tablename__ = 'Statuses'

    Id = Column(Integer, primary_key=True)
    StatusName = Column(String, nullable=True)