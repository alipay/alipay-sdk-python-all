#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProjectInfo import ProjectInfo


class AlipayCommerceMedicalInsuranceRiskinfoSyncModel(object):

    def __init__(self):
        self._company_type = None
        self._effect_end_time = None
        self._effect_start_time = None
        self._equity_settle_start_time = None
        self._old_serial_no = None
        self._organization_code = None
        self._parent_serial_no = None
        self._parent_status = None
        self._pay_time = None
        self._prod_no = None
        self._project_list = None
        self._sales_method = None
        self._serial_no = None
        self._status = None

    @property
    def company_type(self):
        return self._company_type

    @company_type.setter
    def company_type(self, value):
        self._company_type = value
    @property
    def effect_end_time(self):
        return self._effect_end_time

    @effect_end_time.setter
    def effect_end_time(self, value):
        self._effect_end_time = value
    @property
    def effect_start_time(self):
        return self._effect_start_time

    @effect_start_time.setter
    def effect_start_time(self, value):
        self._effect_start_time = value
    @property
    def equity_settle_start_time(self):
        return self._equity_settle_start_time

    @equity_settle_start_time.setter
    def equity_settle_start_time(self, value):
        self._equity_settle_start_time = value
    @property
    def old_serial_no(self):
        return self._old_serial_no

    @old_serial_no.setter
    def old_serial_no(self, value):
        self._old_serial_no = value
    @property
    def organization_code(self):
        return self._organization_code

    @organization_code.setter
    def organization_code(self, value):
        self._organization_code = value
    @property
    def parent_serial_no(self):
        return self._parent_serial_no

    @parent_serial_no.setter
    def parent_serial_no(self, value):
        self._parent_serial_no = value
    @property
    def parent_status(self):
        return self._parent_status

    @parent_status.setter
    def parent_status(self, value):
        self._parent_status = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def prod_no(self):
        return self._prod_no

    @prod_no.setter
    def prod_no(self, value):
        self._prod_no = value
    @property
    def project_list(self):
        return self._project_list

    @project_list.setter
    def project_list(self, value):
        if isinstance(value, list):
            self._project_list = list()
            for i in value:
                if isinstance(i, ProjectInfo):
                    self._project_list.append(i)
                else:
                    self._project_list.append(ProjectInfo.from_alipay_dict(i))
    @property
    def sales_method(self):
        return self._sales_method

    @sales_method.setter
    def sales_method(self, value):
        self._sales_method = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_type:
            if hasattr(self.company_type, 'to_alipay_dict'):
                params['company_type'] = self.company_type.to_alipay_dict()
            else:
                params['company_type'] = self.company_type
        if self.effect_end_time:
            if hasattr(self.effect_end_time, 'to_alipay_dict'):
                params['effect_end_time'] = self.effect_end_time.to_alipay_dict()
            else:
                params['effect_end_time'] = self.effect_end_time
        if self.effect_start_time:
            if hasattr(self.effect_start_time, 'to_alipay_dict'):
                params['effect_start_time'] = self.effect_start_time.to_alipay_dict()
            else:
                params['effect_start_time'] = self.effect_start_time
        if self.equity_settle_start_time:
            if hasattr(self.equity_settle_start_time, 'to_alipay_dict'):
                params['equity_settle_start_time'] = self.equity_settle_start_time.to_alipay_dict()
            else:
                params['equity_settle_start_time'] = self.equity_settle_start_time
        if self.old_serial_no:
            if hasattr(self.old_serial_no, 'to_alipay_dict'):
                params['old_serial_no'] = self.old_serial_no.to_alipay_dict()
            else:
                params['old_serial_no'] = self.old_serial_no
        if self.organization_code:
            if hasattr(self.organization_code, 'to_alipay_dict'):
                params['organization_code'] = self.organization_code.to_alipay_dict()
            else:
                params['organization_code'] = self.organization_code
        if self.parent_serial_no:
            if hasattr(self.parent_serial_no, 'to_alipay_dict'):
                params['parent_serial_no'] = self.parent_serial_no.to_alipay_dict()
            else:
                params['parent_serial_no'] = self.parent_serial_no
        if self.parent_status:
            if hasattr(self.parent_status, 'to_alipay_dict'):
                params['parent_status'] = self.parent_status.to_alipay_dict()
            else:
                params['parent_status'] = self.parent_status
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.prod_no:
            if hasattr(self.prod_no, 'to_alipay_dict'):
                params['prod_no'] = self.prod_no.to_alipay_dict()
            else:
                params['prod_no'] = self.prod_no
        if self.project_list:
            if isinstance(self.project_list, list):
                for i in range(0, len(self.project_list)):
                    element = self.project_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.project_list[i] = element.to_alipay_dict()
            if hasattr(self.project_list, 'to_alipay_dict'):
                params['project_list'] = self.project_list.to_alipay_dict()
            else:
                params['project_list'] = self.project_list
        if self.sales_method:
            if hasattr(self.sales_method, 'to_alipay_dict'):
                params['sales_method'] = self.sales_method.to_alipay_dict()
            else:
                params['sales_method'] = self.sales_method
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceRiskinfoSyncModel()
        if 'company_type' in d:
            o.company_type = d['company_type']
        if 'effect_end_time' in d:
            o.effect_end_time = d['effect_end_time']
        if 'effect_start_time' in d:
            o.effect_start_time = d['effect_start_time']
        if 'equity_settle_start_time' in d:
            o.equity_settle_start_time = d['equity_settle_start_time']
        if 'old_serial_no' in d:
            o.old_serial_no = d['old_serial_no']
        if 'organization_code' in d:
            o.organization_code = d['organization_code']
        if 'parent_serial_no' in d:
            o.parent_serial_no = d['parent_serial_no']
        if 'parent_status' in d:
            o.parent_status = d['parent_status']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'prod_no' in d:
            o.prod_no = d['prod_no']
        if 'project_list' in d:
            o.project_list = d['project_list']
        if 'sales_method' in d:
            o.sales_method = d['sales_method']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'status' in d:
            o.status = d['status']
        return o


