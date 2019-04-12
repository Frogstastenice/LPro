from db_classes import ApplicationStatusHistory
from db_classes import Status
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

class DbBase:
    def get_session(self):
        engine = db.create_engine('mssql+pyodbc://pretender:nAJK9bqo$%4Gi^w34Xko@machineslearn.database.windows.net/TestPythonAnalytics?driver=ODBC+Driver+13+for+SQL+Server')
        Session = sessionmaker(bind=engine)
        #Session.configure(bind=engine)
        session = Session()
        return session

class StatusManager(DbBase):
    def load_statuses(self):
        self.statuses_dict = {}
        self.status_color_dict = {}
        self.termination_statuses = {391056, 458323}
        
        session = self.get_session()

        for row in session.query(Status):
            status_id = row.Id
            if status_id in {267, 268, 269, 270, 2459}:
                self.statuses_dict[status_id] = 'Экспресс-оценка'
            elif status_id in {271, 458325, 458326}:
                self.statuses_dict[status_id] = 'Входная экспертиза'
            elif status_id in {272, 273, 274, 458327}:
                self.statuses_dict[status_id] = 'Комплексная экспертиза'
            elif status_id in {275, 276, 277, 278, 458328}:
                self.statuses_dict[status_id] = 'Экспертный совет'
            elif status_id in {279, 20761, 192134, 192135}:
                self.statuses_dict[status_id] = 'Выдача займов'

            # Это костыль!
            self.statuses_dict[None] = 'Херня'

            if status_id in {458326, 274, 276, 269}:
                self.status_color_dict[status_id] = 'Дорабатывается'
            elif status_id in {458325, 279, 273, 458327, 275, 268, 2459}:
                self.status_color_dict[status_id] = 'На рассмотрении'
            elif status_id in {192134, 277, 270}:
                self.status_color_dict[status_id] = 'Отклонен'
            elif status_id in {271, 272, 192135, 278, 458328}:
                self.status_color_dict[status_id] = 'Подготовка документов'
            elif status_id in {20761}:
                self.status_color_dict[status_id] = 'Пройден'

            # Это костыль!
            self.status_color_dict[None] = 'Херня'

    def get_stage_by_status(self, status_history_row):
        if status_history_row.IdCurrentStatus in self.termination_statuses:
            return self.statuses_dict[status_history_row.IdPreviousStatus]
        else:
            return self.statuses_dict[status_history_row.IdCurrentStatus]

    def get_color_by_status(self, status_history_row):
        return self.status_color_dict[status_history_row.IdCurrentStatus]

    def get_all_stages(self):
        return list(sorted(self.statuses_dict.values()))

class ApplicationDataRetriever(DbBase):
    def get_applications_by_dates(self, start_date, end_date):
        session = self.get_session()
        result = []
        for row in session.query(ApplicationStatusHistory):
            if row.StatusBeginDate < start_date:
                if row.StatusEndDate >= start_date:
                    result.append(row)
            elif row.StatusBeginDate <= end_date:
                result.append(row)
        
        return result

