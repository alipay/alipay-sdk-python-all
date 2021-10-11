#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceAssetmanagePenetratebillQueryModel(object):

    def __init__(self):
        self._agreement_code = None
        self._bill_date = None
        self._bill_period = None

    @property
    def agreement_code(self):
        return self._agreement_code

    @agreement_code.setter
    def agreement_code(self, value):
        self._agreement_code = value
    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def bill_period(self):
        return self._bill_period

    @bill_period.setter
    def bill_period(self, value):
        self._bill_period = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_code:
            if hasattr(self.agreement_code, 'to_alipay_dict'):
                params['agreement_code'] = self.agreement_code.to_alipay_dict()
            else:
                params['agreement_code'] = self.agreement_code
        if self.bill_date:
            if hasattr(self.bill_date, 'to_alipay_dict'):
                params['bill_date'] = self.bill_date.to_alipay_dict()
            else:
                params['bill_date'] = self.bill_date
        if self.bill_period:
            if hasattr(self.bill_period, 'to_alipay_dict'):
                params['bill_period'] = self.bill_period.to_alipay_dict()
            else:
                params['bill_period'] = self.bill_period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceAssetmanagePenetratebillQueryModel()
        if 'agreement_code' in d:
            o.agreement_code = d['agreement_code']
        if 'bill_date' in d:
            o.bill_date = d['bill_date']
        if 'bill_period' in d:
            o.bill_period = d['bill_period']
        return o


