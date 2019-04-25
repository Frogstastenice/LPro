from constants import StageStatusConstants, TerminationStatusConstants, ColorStatusConstants
from db_classes import ApplicationStatusHistory, Application, Industry, ReportIndustry, Status
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_
import config

class DbBase:
    def get_session(self):
        engine = db.create_engine(config.DB_DSN)
        Session = sessionmaker(bind=engine)
        #Session.configure(bind=engine)
        session = Session()
        return session

class StatusManager(DbBase):
    def load_statuses(self):
        self.statuses_dict = {}
        self.status_color_dict = {}
                
        session = self.get_session()

        for row in session.query(Status):
            status_id = row.Id
            if status_id in StageStatusConstants.ExpressEval:
                self.statuses_dict[status_id] = 'Экспресс-оценка'
            elif status_id in StageStatusConstants.EntryExp:
                self.statuses_dict[status_id] = 'Входная экспертиза'
            elif status_id in StageStatusConstants.ComplexExp:
                self.statuses_dict[status_id] = 'Комплексная экспертиза'
            elif status_id in StageStatusConstants.ExpCouncil:
                self.statuses_dict[status_id] = 'Экспертный совет'
            elif status_id in StageStatusConstants.LoanIssue:
                self.statuses_dict[status_id] = 'Выдача займов'

            if status_id in ColorStatusConstants.Refinement:
                self.status_color_dict[status_id] = 'Дорабатывается'
            elif status_id in ColorStatusConstants.OnApproval:
                self.status_color_dict[status_id] = 'На рассмотрении'
            elif status_id in ColorStatusConstants.Denied:
                self.status_color_dict[status_id] = 'Отклонен'
            elif status_id in ColorStatusConstants.DocProcessing:
                self.status_color_dict[status_id] = 'Подготовка документов'
            elif status_id in ColorStatusConstants.LoanReceived:
                self.status_color_dict[status_id] = 'Пройден'
            elif status_id == TerminationStatusConstants.TerminatedStatus:
                self.status_color_dict[status_id] = 'Проект прекращен'
            elif status_id == TerminationStatusConstants.PausedStatus:
                self.status_color_dict[status_id] = 'Проект приостановлен'

    def get_valid_statuses(self):
        stages = set(self.statuses_dict.keys())
        status_color = set(self.status_color_dict.keys())

        return stages.intersection(status_color).union(TerminationStatusConstants.TerminationStatuses)

    def get_stage_by_status(self, status_history_row):
        if status_history_row.IdCurrentStatus in TerminationStatusConstants.TerminationStatuses:
            return self.statuses_dict[status_history_row.IdPreviousStatus]
        else:
            return self.statuses_dict[status_history_row.IdCurrentStatus]

    def get_color_by_status(self, status_history_row):
        return self.status_color_dict[status_history_row.IdCurrentStatus]

    def get_all_stages(self):
        return list(sorted(set(self.statuses_dict.values())))

    def get_all_colors(self):
        return sorted(set(self.status_color_dict.values()))

class ApplicationStatusManager(DbBase):
    def get_applications_by_dates(self, start_date, end_date, valid_statuses):
        session = self.get_session()
        result = []
        statusFilter = and_(
            ApplicationStatusHistory.IdCurrentStatus.in_(valid_statuses),
            and_(
                or_(
                    ApplicationStatusHistory.IdPreviousStatus.is_(None),
                    ~ApplicationStatusHistory.IdPreviousStatus.in_(TerminationStatusConstants.TerminationStatuses)
                ),
                or_(
                    ApplicationStatusHistory.IdPreviousStatus.in_(valid_statuses),
                    and_(
                        ApplicationStatusHistory.IdPreviousStatus.is_(None),
                        ~ApplicationStatusHistory.IdCurrentStatus.in_(TerminationStatusConstants.TerminationStatuses)
                    )
                )
            )
        )
        dateFilter = or_(
            and_(
                ApplicationStatusHistory.StatusBeginDate < start_date, 
                or_(
                    ApplicationStatusHistory.StatusEndDate.is_(None),
                    ApplicationStatusHistory.StatusEndDate >= start_date
                )
            ),
            and_(
                ApplicationStatusHistory.StatusBeginDate <= end_date,
                ApplicationStatusHistory.StatusBeginDate >= start_date
            )
        )
        
        filterExpression = and_(
            statusFilter,
            dateFilter
        )

        #ifs = []

        # for row in session.query(ApplicationStatusHistory).filter(statusFilter):
        #     if row.StatusBeginDate < start_date:
        #         if row.StatusEndDate is None or row.StatusEndDate >= start_date:
        #             ifs.append(row)
        #     elif row.StatusBeginDate <= end_date:
        #         ifs.append(row)

        result = session.query(ApplicationStatusHistory).filter(filterExpression).all()

        # rids = {row.Id for row in result}
        # iids = {row.Id for row in ifs}
        # diff = iids.symmetric_difference(rids)

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

