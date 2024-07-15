#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CorpShareholderTotal(object):

    def __init__(self):
        self._funding_method = None
        self._paid_currency = None
        self._shareholding_percent = None
        self._shareholding_type = None
        self._shares_num = None

    @property
    def funding_method(self):
        return self._funding_method

    @funding_method.setter
    def funding_method(self, value):
        self._funding_method = value
    @property
    def paid_currency(self):
        return self._paid_currency

    @paid_currency.setter
    def paid_currency(self, value):
        self._paid_currency = value
    @property
    def shareholding_percent(self):
        return self._shareholding_percent

    @shareholding_percent.setter
    def shareholding_percent(self, value):
        self._shareholding_percent = value
    @property
    def shareholding_type(self):
        return self._shareholding_type

    @shareholding_type.setter
    def shareholding_type(self, value):
        self._shareholding_type = value
    @property
    def shares_num(self):
        return self._shares_num

    @shares_num.setter
    def shares_num(self, value):
        self._shares_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.funding_method:
            if hasattr(self.funding_method, 'to_alipay_dict'):
                params['funding_method'] = self.funding_method.to_alipay_dict()
            else:
                params['funding_method'] = self.funding_method
        if self.paid_currency:
            if hasattr(self.paid_currency, 'to_alipay_dict'):
                params['paid_currency'] = self.paid_currency.to_alipay_dict()
            else:
                params['paid_currency'] = self.paid_currency
        if self.shareholding_percent:
            if hasattr(self.shareholding_percent, 'to_alipay_dict'):
                params['shareholding_percent'] = self.shareholding_percent.to_alipay_dict()
            else:
                params['shareholding_percent'] = self.shareholding_percent
        if self.shareholding_type:
            if hasattr(self.shareholding_type, 'to_alipay_dict'):
                params['shareholding_type'] = self.shareholding_type.to_alipay_dict()
            else:
                params['shareholding_type'] = self.shareholding_type
        if self.shares_num:
            if hasattr(self.shares_num, 'to_alipay_dict'):
                params['shares_num'] = self.shares_num.to_alipay_dict()
            else:
                params['shares_num'] = self.shares_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CorpShareholderTotal()
        if 'funding_method' in d:
            o.funding_method = d['funding_method']
        if 'paid_currency' in d:
            o.paid_currency = d['paid_currency']
        if 'shareholding_percent' in d:
            o.shareholding_percent = d['shareholding_percent']
        if 'shareholding_type' in d:
            o.shareholding_type = d['shareholding_type']
        if 'shares_num' in d:
            o.shares_num = d['shares_num']
        return o


