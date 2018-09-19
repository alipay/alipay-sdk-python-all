#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YLBPriceDetailInfo(object):

    def __init__(self):
        self._price_date = None
        self._sevendays_yeild_rate = None
        self._tenthousand_income = None

    @property
    def price_date(self):
        return self._price_date

    @price_date.setter
    def price_date(self, value):
        self._price_date = value
    @property
    def sevendays_yeild_rate(self):
        return self._sevendays_yeild_rate

    @sevendays_yeild_rate.setter
    def sevendays_yeild_rate(self, value):
        self._sevendays_yeild_rate = value
    @property
    def tenthousand_income(self):
        return self._tenthousand_income

    @tenthousand_income.setter
    def tenthousand_income(self, value):
        self._tenthousand_income = value


    def to_alipay_dict(self):
        params = dict()
        if self.price_date:
            if hasattr(self.price_date, 'to_alipay_dict'):
                params['price_date'] = self.price_date.to_alipay_dict()
            else:
                params['price_date'] = self.price_date
        if self.sevendays_yeild_rate:
            if hasattr(self.sevendays_yeild_rate, 'to_alipay_dict'):
                params['sevendays_yeild_rate'] = self.sevendays_yeild_rate.to_alipay_dict()
            else:
                params['sevendays_yeild_rate'] = self.sevendays_yeild_rate
        if self.tenthousand_income:
            if hasattr(self.tenthousand_income, 'to_alipay_dict'):
                params['tenthousand_income'] = self.tenthousand_income.to_alipay_dict()
            else:
                params['tenthousand_income'] = self.tenthousand_income
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YLBPriceDetailInfo()
        if 'price_date' in d:
            o.price_date = d['price_date']
        if 'sevendays_yeild_rate' in d:
            o.sevendays_yeild_rate = d['sevendays_yeild_rate']
        if 'tenthousand_income' in d:
            o.tenthousand_income = d['tenthousand_income']
        return o


