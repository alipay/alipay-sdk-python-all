#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class ApInvoiceBillLinkOrderRequest(object):

    def __init__(self):
        self._amt = None
        self._daily_bill_dimension = None
        self._monthly_bill_no = None

    @property
    def amt(self):
        return self._amt

    @amt.setter
    def amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._amt = value
        else:
            self._amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def daily_bill_dimension(self):
        return self._daily_bill_dimension

    @daily_bill_dimension.setter
    def daily_bill_dimension(self, value):
        self._daily_bill_dimension = value
    @property
    def monthly_bill_no(self):
        return self._monthly_bill_no

    @monthly_bill_no.setter
    def monthly_bill_no(self, value):
        self._monthly_bill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amt:
            if hasattr(self.amt, 'to_alipay_dict'):
                params['amt'] = self.amt.to_alipay_dict()
            else:
                params['amt'] = self.amt
        if self.daily_bill_dimension:
            if hasattr(self.daily_bill_dimension, 'to_alipay_dict'):
                params['daily_bill_dimension'] = self.daily_bill_dimension.to_alipay_dict()
            else:
                params['daily_bill_dimension'] = self.daily_bill_dimension
        if self.monthly_bill_no:
            if hasattr(self.monthly_bill_no, 'to_alipay_dict'):
                params['monthly_bill_no'] = self.monthly_bill_no.to_alipay_dict()
            else:
                params['monthly_bill_no'] = self.monthly_bill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApInvoiceBillLinkOrderRequest()
        if 'amt' in d:
            o.amt = d['amt']
        if 'daily_bill_dimension' in d:
            o.daily_bill_dimension = d['daily_bill_dimension']
        if 'monthly_bill_no' in d:
            o.monthly_bill_no = d['monthly_bill_no']
        return o


