#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StockHolderVO(object):

    def __init__(self):
        self._invest_date = None
        self._invest_rate = None
        self._org_holder_name = None
        self._org_holder_type = None
        self._subscript_amt = None
        self._subscript_amt_curcy = None

    @property
    def invest_date(self):
        return self._invest_date

    @invest_date.setter
    def invest_date(self, value):
        self._invest_date = value
    @property
    def invest_rate(self):
        return self._invest_rate

    @invest_rate.setter
    def invest_rate(self, value):
        self._invest_rate = value
    @property
    def org_holder_name(self):
        return self._org_holder_name

    @org_holder_name.setter
    def org_holder_name(self, value):
        self._org_holder_name = value
    @property
    def org_holder_type(self):
        return self._org_holder_type

    @org_holder_type.setter
    def org_holder_type(self, value):
        self._org_holder_type = value
    @property
    def subscript_amt(self):
        return self._subscript_amt

    @subscript_amt.setter
    def subscript_amt(self, value):
        self._subscript_amt = value
    @property
    def subscript_amt_curcy(self):
        return self._subscript_amt_curcy

    @subscript_amt_curcy.setter
    def subscript_amt_curcy(self, value):
        self._subscript_amt_curcy = value


    def to_alipay_dict(self):
        params = dict()
        if self.invest_date:
            if hasattr(self.invest_date, 'to_alipay_dict'):
                params['invest_date'] = self.invest_date.to_alipay_dict()
            else:
                params['invest_date'] = self.invest_date
        if self.invest_rate:
            if hasattr(self.invest_rate, 'to_alipay_dict'):
                params['invest_rate'] = self.invest_rate.to_alipay_dict()
            else:
                params['invest_rate'] = self.invest_rate
        if self.org_holder_name:
            if hasattr(self.org_holder_name, 'to_alipay_dict'):
                params['org_holder_name'] = self.org_holder_name.to_alipay_dict()
            else:
                params['org_holder_name'] = self.org_holder_name
        if self.org_holder_type:
            if hasattr(self.org_holder_type, 'to_alipay_dict'):
                params['org_holder_type'] = self.org_holder_type.to_alipay_dict()
            else:
                params['org_holder_type'] = self.org_holder_type
        if self.subscript_amt:
            if hasattr(self.subscript_amt, 'to_alipay_dict'):
                params['subscript_amt'] = self.subscript_amt.to_alipay_dict()
            else:
                params['subscript_amt'] = self.subscript_amt
        if self.subscript_amt_curcy:
            if hasattr(self.subscript_amt_curcy, 'to_alipay_dict'):
                params['subscript_amt_curcy'] = self.subscript_amt_curcy.to_alipay_dict()
            else:
                params['subscript_amt_curcy'] = self.subscript_amt_curcy
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StockHolderVO()
        if 'invest_date' in d:
            o.invest_date = d['invest_date']
        if 'invest_rate' in d:
            o.invest_rate = d['invest_rate']
        if 'org_holder_name' in d:
            o.org_holder_name = d['org_holder_name']
        if 'org_holder_type' in d:
            o.org_holder_type = d['org_holder_type']
        if 'subscript_amt' in d:
            o.subscript_amt = d['subscript_amt']
        if 'subscript_amt_curcy' in d:
            o.subscript_amt_curcy = d['subscript_amt_curcy']
        return o


