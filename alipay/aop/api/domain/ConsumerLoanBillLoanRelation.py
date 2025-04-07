#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsumerLoanBillLoanRelation(object):

    def __init__(self):
        self._loan_id = None
        self._period_no = None

    @property
    def loan_id(self):
        return self._loan_id

    @loan_id.setter
    def loan_id(self, value):
        self._loan_id = value
    @property
    def period_no(self):
        return self._period_no

    @period_no.setter
    def period_no(self, value):
        self._period_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.loan_id:
            if hasattr(self.loan_id, 'to_alipay_dict'):
                params['loan_id'] = self.loan_id.to_alipay_dict()
            else:
                params['loan_id'] = self.loan_id
        if self.period_no:
            if hasattr(self.period_no, 'to_alipay_dict'):
                params['period_no'] = self.period_no.to_alipay_dict()
            else:
                params['period_no'] = self.period_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsumerLoanBillLoanRelation()
        if 'loan_id' in d:
            o.loan_id = d['loan_id']
        if 'period_no' in d:
            o.period_no = d['period_no']
        return o


