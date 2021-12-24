#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceEnterpriseconsumeConsumeBatchqueryModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._consumption_end = None
        self._consumption_start = None
        self._employee_list = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def consumption_end(self):
        return self._consumption_end

    @consumption_end.setter
    def consumption_end(self, value):
        self._consumption_end = value
    @property
    def consumption_start(self):
        return self._consumption_start

    @consumption_start.setter
    def consumption_start(self, value):
        self._consumption_start = value
    @property
    def employee_list(self):
        return self._employee_list

    @employee_list.setter
    def employee_list(self, value):
        if isinstance(value, list):
            self._employee_list = list()
            for i in value:
                self._employee_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.consumption_end:
            if hasattr(self.consumption_end, 'to_alipay_dict'):
                params['consumption_end'] = self.consumption_end.to_alipay_dict()
            else:
                params['consumption_end'] = self.consumption_end
        if self.consumption_start:
            if hasattr(self.consumption_start, 'to_alipay_dict'):
                params['consumption_start'] = self.consumption_start.to_alipay_dict()
            else:
                params['consumption_start'] = self.consumption_start
        if self.employee_list:
            if isinstance(self.employee_list, list):
                for i in range(0, len(self.employee_list)):
                    element = self.employee_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.employee_list[i] = element.to_alipay_dict()
            if hasattr(self.employee_list, 'to_alipay_dict'):
                params['employee_list'] = self.employee_list.to_alipay_dict()
            else:
                params['employee_list'] = self.employee_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceEnterpriseconsumeConsumeBatchqueryModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'consumption_end' in d:
            o.consumption_end = d['consumption_end']
        if 'consumption_start' in d:
            o.consumption_start = d['consumption_start']
        if 'employee_list' in d:
            o.employee_list = d['employee_list']
        return o


