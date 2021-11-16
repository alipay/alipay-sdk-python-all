#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Deliverable import Deliverable
from alipay.aop.api.domain.ProjectTimeTable import ProjectTimeTable
from alipay.aop.api.domain.Workload import Workload


class GrmProjectInfoDTO(object):

    def __init__(self):
        self._attachments_url = None
        self._continue_project_code = None
        self._create = None
        self._create_name = None
        self._critical_deliverable = None
        self._description = None
        self._end_date = None
        self._owner = None
        self._owner_name = None
        self._pm = None
        self._pm_name = None
        self._pr_emp_id = None
        self._pr_emp_name = None
        self._project_code = None
        self._project_detail_url = None
        self._project_name = None
        self._project_pay = None
        self._project_time_sheet = None
        self._project_type = None
        self._project_workload = None
        self._service_location = None
        self._settlement_formula_code = None
        self._settlement_formula_name = None
        self._sla_view_info = None
        self._start_date = None
        self._total_amount = None
        self._usage_code = None

    @property
    def attachments_url(self):
        return self._attachments_url

    @attachments_url.setter
    def attachments_url(self, value):
        if isinstance(value, list):
            self._attachments_url = list()
            for i in value:
                self._attachments_url.append(i)
    @property
    def continue_project_code(self):
        return self._continue_project_code

    @continue_project_code.setter
    def continue_project_code(self, value):
        self._continue_project_code = value
    @property
    def create(self):
        return self._create

    @create.setter
    def create(self, value):
        self._create = value
    @property
    def create_name(self):
        return self._create_name

    @create_name.setter
    def create_name(self, value):
        self._create_name = value
    @property
    def critical_deliverable(self):
        return self._critical_deliverable

    @critical_deliverable.setter
    def critical_deliverable(self, value):
        if isinstance(value, list):
            self._critical_deliverable = list()
            for i in value:
                if isinstance(i, Deliverable):
                    self._critical_deliverable.append(i)
                else:
                    self._critical_deliverable.append(Deliverable.from_alipay_dict(i))
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value
    @property
    def pm(self):
        return self._pm

    @pm.setter
    def pm(self, value):
        self._pm = value
    @property
    def pm_name(self):
        return self._pm_name

    @pm_name.setter
    def pm_name(self, value):
        self._pm_name = value
    @property
    def pr_emp_id(self):
        return self._pr_emp_id

    @pr_emp_id.setter
    def pr_emp_id(self, value):
        self._pr_emp_id = value
    @property
    def pr_emp_name(self):
        return self._pr_emp_name

    @pr_emp_name.setter
    def pr_emp_name(self, value):
        self._pr_emp_name = value
    @property
    def project_code(self):
        return self._project_code

    @project_code.setter
    def project_code(self, value):
        self._project_code = value
    @property
    def project_detail_url(self):
        return self._project_detail_url

    @project_detail_url.setter
    def project_detail_url(self, value):
        self._project_detail_url = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value
    @property
    def project_pay(self):
        return self._project_pay

    @project_pay.setter
    def project_pay(self, value):
        self._project_pay = value
    @property
    def project_time_sheet(self):
        return self._project_time_sheet

    @project_time_sheet.setter
    def project_time_sheet(self, value):
        if isinstance(value, list):
            self._project_time_sheet = list()
            for i in value:
                if isinstance(i, ProjectTimeTable):
                    self._project_time_sheet.append(i)
                else:
                    self._project_time_sheet.append(ProjectTimeTable.from_alipay_dict(i))
    @property
    def project_type(self):
        return self._project_type

    @project_type.setter
    def project_type(self, value):
        self._project_type = value
    @property
    def project_workload(self):
        return self._project_workload

    @project_workload.setter
    def project_workload(self, value):
        if isinstance(value, list):
            self._project_workload = list()
            for i in value:
                if isinstance(i, Workload):
                    self._project_workload.append(i)
                else:
                    self._project_workload.append(Workload.from_alipay_dict(i))
    @property
    def service_location(self):
        return self._service_location

    @service_location.setter
    def service_location(self, value):
        self._service_location = value
    @property
    def settlement_formula_code(self):
        return self._settlement_formula_code

    @settlement_formula_code.setter
    def settlement_formula_code(self, value):
        self._settlement_formula_code = value
    @property
    def settlement_formula_name(self):
        return self._settlement_formula_name

    @settlement_formula_name.setter
    def settlement_formula_name(self, value):
        self._settlement_formula_name = value
    @property
    def sla_view_info(self):
        return self._sla_view_info

    @sla_view_info.setter
    def sla_view_info(self, value):
        self._sla_view_info = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def usage_code(self):
        return self._usage_code

    @usage_code.setter
    def usage_code(self, value):
        self._usage_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachments_url:
            if isinstance(self.attachments_url, list):
                for i in range(0, len(self.attachments_url)):
                    element = self.attachments_url[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachments_url[i] = element.to_alipay_dict()
            if hasattr(self.attachments_url, 'to_alipay_dict'):
                params['attachments_url'] = self.attachments_url.to_alipay_dict()
            else:
                params['attachments_url'] = self.attachments_url
        if self.continue_project_code:
            if hasattr(self.continue_project_code, 'to_alipay_dict'):
                params['continue_project_code'] = self.continue_project_code.to_alipay_dict()
            else:
                params['continue_project_code'] = self.continue_project_code
        if self.create:
            if hasattr(self.create, 'to_alipay_dict'):
                params['create'] = self.create.to_alipay_dict()
            else:
                params['create'] = self.create
        if self.create_name:
            if hasattr(self.create_name, 'to_alipay_dict'):
                params['create_name'] = self.create_name.to_alipay_dict()
            else:
                params['create_name'] = self.create_name
        if self.critical_deliverable:
            if isinstance(self.critical_deliverable, list):
                for i in range(0, len(self.critical_deliverable)):
                    element = self.critical_deliverable[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.critical_deliverable[i] = element.to_alipay_dict()
            if hasattr(self.critical_deliverable, 'to_alipay_dict'):
                params['critical_deliverable'] = self.critical_deliverable.to_alipay_dict()
            else:
                params['critical_deliverable'] = self.critical_deliverable
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.owner:
            if hasattr(self.owner, 'to_alipay_dict'):
                params['owner'] = self.owner.to_alipay_dict()
            else:
                params['owner'] = self.owner
        if self.owner_name:
            if hasattr(self.owner_name, 'to_alipay_dict'):
                params['owner_name'] = self.owner_name.to_alipay_dict()
            else:
                params['owner_name'] = self.owner_name
        if self.pm:
            if hasattr(self.pm, 'to_alipay_dict'):
                params['pm'] = self.pm.to_alipay_dict()
            else:
                params['pm'] = self.pm
        if self.pm_name:
            if hasattr(self.pm_name, 'to_alipay_dict'):
                params['pm_name'] = self.pm_name.to_alipay_dict()
            else:
                params['pm_name'] = self.pm_name
        if self.pr_emp_id:
            if hasattr(self.pr_emp_id, 'to_alipay_dict'):
                params['pr_emp_id'] = self.pr_emp_id.to_alipay_dict()
            else:
                params['pr_emp_id'] = self.pr_emp_id
        if self.pr_emp_name:
            if hasattr(self.pr_emp_name, 'to_alipay_dict'):
                params['pr_emp_name'] = self.pr_emp_name.to_alipay_dict()
            else:
                params['pr_emp_name'] = self.pr_emp_name
        if self.project_code:
            if hasattr(self.project_code, 'to_alipay_dict'):
                params['project_code'] = self.project_code.to_alipay_dict()
            else:
                params['project_code'] = self.project_code
        if self.project_detail_url:
            if hasattr(self.project_detail_url, 'to_alipay_dict'):
                params['project_detail_url'] = self.project_detail_url.to_alipay_dict()
            else:
                params['project_detail_url'] = self.project_detail_url
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        if self.project_pay:
            if hasattr(self.project_pay, 'to_alipay_dict'):
                params['project_pay'] = self.project_pay.to_alipay_dict()
            else:
                params['project_pay'] = self.project_pay
        if self.project_time_sheet:
            if isinstance(self.project_time_sheet, list):
                for i in range(0, len(self.project_time_sheet)):
                    element = self.project_time_sheet[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.project_time_sheet[i] = element.to_alipay_dict()
            if hasattr(self.project_time_sheet, 'to_alipay_dict'):
                params['project_time_sheet'] = self.project_time_sheet.to_alipay_dict()
            else:
                params['project_time_sheet'] = self.project_time_sheet
        if self.project_type:
            if hasattr(self.project_type, 'to_alipay_dict'):
                params['project_type'] = self.project_type.to_alipay_dict()
            else:
                params['project_type'] = self.project_type
        if self.project_workload:
            if isinstance(self.project_workload, list):
                for i in range(0, len(self.project_workload)):
                    element = self.project_workload[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.project_workload[i] = element.to_alipay_dict()
            if hasattr(self.project_workload, 'to_alipay_dict'):
                params['project_workload'] = self.project_workload.to_alipay_dict()
            else:
                params['project_workload'] = self.project_workload
        if self.service_location:
            if hasattr(self.service_location, 'to_alipay_dict'):
                params['service_location'] = self.service_location.to_alipay_dict()
            else:
                params['service_location'] = self.service_location
        if self.settlement_formula_code:
            if hasattr(self.settlement_formula_code, 'to_alipay_dict'):
                params['settlement_formula_code'] = self.settlement_formula_code.to_alipay_dict()
            else:
                params['settlement_formula_code'] = self.settlement_formula_code
        if self.settlement_formula_name:
            if hasattr(self.settlement_formula_name, 'to_alipay_dict'):
                params['settlement_formula_name'] = self.settlement_formula_name.to_alipay_dict()
            else:
                params['settlement_formula_name'] = self.settlement_formula_name
        if self.sla_view_info:
            if hasattr(self.sla_view_info, 'to_alipay_dict'):
                params['sla_view_info'] = self.sla_view_info.to_alipay_dict()
            else:
                params['sla_view_info'] = self.sla_view_info
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.usage_code:
            if hasattr(self.usage_code, 'to_alipay_dict'):
                params['usage_code'] = self.usage_code.to_alipay_dict()
            else:
                params['usage_code'] = self.usage_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GrmProjectInfoDTO()
        if 'attachments_url' in d:
            o.attachments_url = d['attachments_url']
        if 'continue_project_code' in d:
            o.continue_project_code = d['continue_project_code']
        if 'create' in d:
            o.create = d['create']
        if 'create_name' in d:
            o.create_name = d['create_name']
        if 'critical_deliverable' in d:
            o.critical_deliverable = d['critical_deliverable']
        if 'description' in d:
            o.description = d['description']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'owner' in d:
            o.owner = d['owner']
        if 'owner_name' in d:
            o.owner_name = d['owner_name']
        if 'pm' in d:
            o.pm = d['pm']
        if 'pm_name' in d:
            o.pm_name = d['pm_name']
        if 'pr_emp_id' in d:
            o.pr_emp_id = d['pr_emp_id']
        if 'pr_emp_name' in d:
            o.pr_emp_name = d['pr_emp_name']
        if 'project_code' in d:
            o.project_code = d['project_code']
        if 'project_detail_url' in d:
            o.project_detail_url = d['project_detail_url']
        if 'project_name' in d:
            o.project_name = d['project_name']
        if 'project_pay' in d:
            o.project_pay = d['project_pay']
        if 'project_time_sheet' in d:
            o.project_time_sheet = d['project_time_sheet']
        if 'project_type' in d:
            o.project_type = d['project_type']
        if 'project_workload' in d:
            o.project_workload = d['project_workload']
        if 'service_location' in d:
            o.service_location = d['service_location']
        if 'settlement_formula_code' in d:
            o.settlement_formula_code = d['settlement_formula_code']
        if 'settlement_formula_name' in d:
            o.settlement_formula_name = d['settlement_formula_name']
        if 'sla_view_info' in d:
            o.sla_view_info = d['sla_view_info']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'usage_code' in d:
            o.usage_code = d['usage_code']
        return o


