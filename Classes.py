from db_classes import ApplicationStatusHistory
from db_classes import Application
from db_classes import Industry
from db_classes import ReportIndustry
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
            elif status_id in {391056}:
                self.status_color_dict[status_id] = 'Проект прекращен'
            elif status_id in {458323}:
                self.status_color_dict[status_id] = 'Проект приостановлен'

    def get_valid_statuses(self):
        return set(self.statuses_dict.keys()).intersection(set(self.status_color_dict.keys())).union(self.termination_statuses)

    def get_stage_by_status(self, status_history_row):
        if status_history_row.IdCurrentStatus in self.termination_statuses:
            return self.statuses_dict[status_history_row.IdPreviousStatus]
        else:
            return self.statuses_dict[status_history_row.IdCurrentStatus]

    def get_color_by_status(self, status_history_row):
        return self.status_color_dict[status_history_row.IdCurrentStatus]

    def get_all_stages(self):
        return list(sorted(set(self.statuses_dict.values())))

    def get_all_colors(self):
        return list(sorted(set(self.status_color_dict.values())))

class ApplicationStatusManager(DbBase):
    def get_applications_by_dates(self, start_date, end_date, valid_statuses):
        session = self.get_session()
        result = []
        for row in session.query(ApplicationStatusHistory):
            if row.IdCurrentStatus is None or not row.IdCurrentStatus in valid_statuses:
                continue
            if not row.IdPreviousStatus is None and not row.IdPreviousStatus in valid_statuses:
                continue
            if row.IdPreviousStatus in {391056, 458323}: # Enough for the demo, lol
                continue
            if row.IdCurrentStatus in {391056, 458323} and row.IdPreviousStatus is None: # Фабрика костылей
                continue
            if row.StatusBeginDate < start_date:
                if row.StatusEndDate is None or row.StatusEndDate >= start_date:
                    result.append(row)
            elif row.StatusBeginDate <= end_date:
                result.append(row)
        
        return result

class IndustryManager(DbBase):
    
    def load_industries(self):
        self.ind_dict_name = {}

        ind_dict = {}
        session = self.get_session()

        for row in session.query(ReportIndustry):
            ind_dict[row.Id] = row.ReportIndustryName.strip()

        for row in session.query(Industry):
            self.ind_dict_name[row.Id] = ind_dict[row.IdReportIndustry]

    def get_report_industry_name(self, industry_id):
        return self.ind_dict_name[industry_id]

            
class ApplicationManager(DbBase):

    def get_applications_by_status(self, statuses):
        session = self.get_session()
        return session.query(Application).filter(Application.IdStatus.in_(statuses)).all()

