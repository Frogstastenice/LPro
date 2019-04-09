class ApplicationStatusHistory:
    def __init__(self, id, idProject, idCurrentStatus, idPreviousStatus, statusBeginDate, statusEndDate):
        self.id = id
        self.idProject = idProject
        self.idCurrentStatus = idCurrentStatus
        self.idPreviousStatus = idPreviousStatus
        self.statusBeginDate = statusBeginDate
        self.statusEndDate = statusEndDate
    
    def __repr__(self):
        return f'Id: {self.id}\nProject Id: {self.idProject}\nCurrent Status: {self.idCurrentStatus}\nPrevious Status: {self.idPreviousStatus}\nStart Date: {self.statusBeginDate}\nEnd Date: {self.statusEndDate}'

#test = ApplicationStatusHistory(42, 102, 12, 11, '01-01-2019', '31-01-2019')
#print(test)
