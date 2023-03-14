#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceExpensecontrolCostassertQueryModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._alipay_bill_no = None
        self._employee_id = None
        self._employee_open_id = None
        self._enterprise_id = None
        self._out_source_id = None
        self._platform = None

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
    def alipay_bill_no(self):
        return self._alipay_bill_no

    @alipay_bill_no.setter
    def alipay_bill_no(self, value):
        self._alipay_bill_no = value
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def employee_open_id(self):
        return self._employee_open_id

    @employee_open_id.setter
    def employee_open_id(self, value):
        self._employee_open_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def out_source_id(self):
        return self._out_source_id

    @out_source_id.setter
    def out_source_id(self, value):
        self._out_source_id = value
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = value


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
        if self.alipay_bill_no:
            if hasattr(self.alipay_bill_no, 'to_alipay_dict'):
                params['alipay_bill_no'] = self.alipay_bill_no.to_alipay_dict()
            else:
                params['alipay_bill_no'] = self.alipay_bill_no
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.employee_open_id:
            if hasattr(self.employee_open_id, 'to_alipay_dict'):
                params['employee_open_id'] = self.employee_open_id.to_alipay_dict()
            else:
                params['employee_open_id'] = self.employee_open_id
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.out_source_id:
            if hasattr(self.out_source_id, 'to_alipay_dict'):
                params['out_source_id'] = self.out_source_id.to_alipay_dict()
            else:
                params['out_source_id'] = self.out_source_id
        if self.platform:
            if hasattr(self.platform, 'to_alipay_dict'):
                params['platform'] = self.platform.to_alipay_dict()
            else:
                params['platform'] = self.platform
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceExpensecontrolCostassertQueryModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'alipay_bill_no' in d:
            o.alipay_bill_no = d['alipay_bill_no']
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'employee_open_id' in d:
            o.employee_open_id = d['employee_open_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'out_source_id' in d:
            o.out_source_id = d['out_source_id']
        if 'platform' in d:
            o.platform = d['platform']
        return o


