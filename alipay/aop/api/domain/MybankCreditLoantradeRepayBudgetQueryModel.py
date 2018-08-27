#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoantradeRepayBudgetQueryModel(object):

    def __init__(self):
        self._apply_repay_prin = None
        self._ext_data = None
        self._ip_id = None
        self._ip_role_id = None
        self._loan_ar_no = None

    @property
    def apply_repay_prin(self):
        return self._apply_repay_prin

    @apply_repay_prin.setter
    def apply_repay_prin(self, value):
        self._apply_repay_prin = value
    @property
    def ext_data(self):
        return self._ext_data

    @ext_data.setter
    def ext_data(self, value):
        self._ext_data = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def loan_ar_no(self):
        return self._loan_ar_no

    @loan_ar_no.setter
    def loan_ar_no(self, value):
        self._loan_ar_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_repay_prin:
            if hasattr(self.apply_repay_prin, 'to_alipay_dict'):
                params['apply_repay_prin'] = self.apply_repay_prin.to_alipay_dict()
            else:
                params['apply_repay_prin'] = self.apply_repay_prin
        if self.ext_data:
            if hasattr(self.ext_data, 'to_alipay_dict'):
                params['ext_data'] = self.ext_data.to_alipay_dict()
            else:
                params['ext_data'] = self.ext_data
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.loan_ar_no:
            if hasattr(self.loan_ar_no, 'to_alipay_dict'):
                params['loan_ar_no'] = self.loan_ar_no.to_alipay_dict()
            else:
                params['loan_ar_no'] = self.loan_ar_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeRepayBudgetQueryModel()
        if 'apply_repay_prin' in d:
            o.apply_repay_prin = d['apply_repay_prin']
        if 'ext_data' in d:
            o.ext_data = d['ext_data']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'loan_ar_no' in d:
            o.loan_ar_no = d['loan_ar_no']
        return o


