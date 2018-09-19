#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoantradeLoanarrangementQueryModel(object):

    def __init__(self):
        self._ip_role_id = None
        self._loan_ar_no = None

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
        o = MybankCreditLoantradeLoanarrangementQueryModel()
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'loan_ar_no' in d:
            o.loan_ar_no = d['loan_ar_no']
        return o


