#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpPaidInDetailInfo(object):

    def __init__(self):
        self._paid_in_contributive_currency = None
        self._paid_in_contributive_date = None
        self._paid_in_contributive_money = None
        self._paid_in_contributive_way = None

    @property
    def paid_in_contributive_currency(self):
        return self._paid_in_contributive_currency

    @paid_in_contributive_currency.setter
    def paid_in_contributive_currency(self, value):
        self._paid_in_contributive_currency = value
    @property
    def paid_in_contributive_date(self):
        return self._paid_in_contributive_date

    @paid_in_contributive_date.setter
    def paid_in_contributive_date(self, value):
        self._paid_in_contributive_date = value
    @property
    def paid_in_contributive_money(self):
        return self._paid_in_contributive_money

    @paid_in_contributive_money.setter
    def paid_in_contributive_money(self, value):
        self._paid_in_contributive_money = value
    @property
    def paid_in_contributive_way(self):
        return self._paid_in_contributive_way

    @paid_in_contributive_way.setter
    def paid_in_contributive_way(self, value):
        self._paid_in_contributive_way = value


    def to_alipay_dict(self):
        params = dict()
        if self.paid_in_contributive_currency:
            if hasattr(self.paid_in_contributive_currency, 'to_alipay_dict'):
                params['paid_in_contributive_currency'] = self.paid_in_contributive_currency.to_alipay_dict()
            else:
                params['paid_in_contributive_currency'] = self.paid_in_contributive_currency
        if self.paid_in_contributive_date:
            if hasattr(self.paid_in_contributive_date, 'to_alipay_dict'):
                params['paid_in_contributive_date'] = self.paid_in_contributive_date.to_alipay_dict()
            else:
                params['paid_in_contributive_date'] = self.paid_in_contributive_date
        if self.paid_in_contributive_money:
            if hasattr(self.paid_in_contributive_money, 'to_alipay_dict'):
                params['paid_in_contributive_money'] = self.paid_in_contributive_money.to_alipay_dict()
            else:
                params['paid_in_contributive_money'] = self.paid_in_contributive_money
        if self.paid_in_contributive_way:
            if hasattr(self.paid_in_contributive_way, 'to_alipay_dict'):
                params['paid_in_contributive_way'] = self.paid_in_contributive_way.to_alipay_dict()
            else:
                params['paid_in_contributive_way'] = self.paid_in_contributive_way
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpPaidInDetailInfo()
        if 'paid_in_contributive_currency' in d:
            o.paid_in_contributive_currency = d['paid_in_contributive_currency']
        if 'paid_in_contributive_date' in d:
            o.paid_in_contributive_date = d['paid_in_contributive_date']
        if 'paid_in_contributive_money' in d:
            o.paid_in_contributive_money = d['paid_in_contributive_money']
        if 'paid_in_contributive_way' in d:
            o.paid_in_contributive_way = d['paid_in_contributive_way']
        return o


