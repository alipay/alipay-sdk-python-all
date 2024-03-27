#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExpenseControlInfo import ExpenseControlInfo


class AlipayCommerceEcSupplierHomepageurlQueryModel(object):

    def __init__(self):
        self._employee_id = None
        self._enterprise_id = None
        self._expense_control_info = None
        self._service_id = None

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def expense_control_info(self):
        return self._expense_control_info

    @expense_control_info.setter
    def expense_control_info(self, value):
        if isinstance(value, ExpenseControlInfo):
            self._expense_control_info = value
        else:
            self._expense_control_info = ExpenseControlInfo.from_alipay_dict(value)
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.expense_control_info:
            if hasattr(self.expense_control_info, 'to_alipay_dict'):
                params['expense_control_info'] = self.expense_control_info.to_alipay_dict()
            else:
                params['expense_control_info'] = self.expense_control_info
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcSupplierHomepageurlQueryModel()
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'expense_control_info' in d:
            o.expense_control_info = d['expense_control_info']
        if 'service_id' in d:
            o.service_id = d['service_id']
        return o


