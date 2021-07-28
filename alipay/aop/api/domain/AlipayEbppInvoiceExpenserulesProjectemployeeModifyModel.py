#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceExpenserulesProjectemployeeModifyModel(object):

    def __init__(self):
        self._account_id = None
        self._add_employee_list = None
        self._agreement_no = None
        self._project_id = None
        self._remove_employee_list = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def add_employee_list(self):
        return self._add_employee_list

    @add_employee_list.setter
    def add_employee_list(self, value):
        if isinstance(value, list):
            self._add_employee_list = list()
            for i in value:
                self._add_employee_list.append(i)
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def remove_employee_list(self):
        return self._remove_employee_list

    @remove_employee_list.setter
    def remove_employee_list(self, value):
        if isinstance(value, list):
            self._remove_employee_list = list()
            for i in value:
                self._remove_employee_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.add_employee_list:
            if isinstance(self.add_employee_list, list):
                for i in range(0, len(self.add_employee_list)):
                    element = self.add_employee_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.add_employee_list[i] = element.to_alipay_dict()
            if hasattr(self.add_employee_list, 'to_alipay_dict'):
                params['add_employee_list'] = self.add_employee_list.to_alipay_dict()
            else:
                params['add_employee_list'] = self.add_employee_list
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.remove_employee_list:
            if isinstance(self.remove_employee_list, list):
                for i in range(0, len(self.remove_employee_list)):
                    element = self.remove_employee_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.remove_employee_list[i] = element.to_alipay_dict()
            if hasattr(self.remove_employee_list, 'to_alipay_dict'):
                params['remove_employee_list'] = self.remove_employee_list.to_alipay_dict()
            else:
                params['remove_employee_list'] = self.remove_employee_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceExpenserulesProjectemployeeModifyModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'add_employee_list' in d:
            o.add_employee_list = d['add_employee_list']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'remove_employee_list' in d:
            o.remove_employee_list = d['remove_employee_list']
        return o


