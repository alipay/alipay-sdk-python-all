#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSceneprodLprQueryModel(object):

    def __init__(self):
        self._loan_rate = None

    @property
    def loan_rate(self):
        return self._loan_rate

    @loan_rate.setter
    def loan_rate(self, value):
        self._loan_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.loan_rate:
            if hasattr(self.loan_rate, 'to_alipay_dict'):
                params['loan_rate'] = self.loan_rate.to_alipay_dict()
            else:
                params['loan_rate'] = self.loan_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSceneprodLprQueryModel()
        if 'loan_rate' in d:
            o.loan_rate = d['loan_rate']
        return o


