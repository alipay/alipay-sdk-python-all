#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZmepAnnualReportShareholderInfo(object):

    def __init__(self):
        self._paid_contributive_date = None
        self._paid_contributive_money = None
        self._paid_contributive_way = None
        self._paid_in_contributive_date = None
        self._paid_in_contributive_money = None
        self._paid_in_contributive_way = None
        self._shareholder = None

    @property
    def paid_contributive_date(self):
        return self._paid_contributive_date

    @paid_contributive_date.setter
    def paid_contributive_date(self, value):
        self._paid_contributive_date = value
    @property
    def paid_contributive_money(self):
        return self._paid_contributive_money

    @paid_contributive_money.setter
    def paid_contributive_money(self, value):
        self._paid_contributive_money = value
    @property
    def paid_contributive_way(self):
        return self._paid_contributive_way

    @paid_contributive_way.setter
    def paid_contributive_way(self, value):
        self._paid_contributive_way = value
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
    @property
    def shareholder(self):
        return self._shareholder

    @shareholder.setter
    def shareholder(self, value):
        self._shareholder = value


    def to_alipay_dict(self):
        params = dict()
        if self.paid_contributive_date:
            if hasattr(self.paid_contributive_date, 'to_alipay_dict'):
                params['paid_contributive_date'] = self.paid_contributive_date.to_alipay_dict()
            else:
                params['paid_contributive_date'] = self.paid_contributive_date
        if self.paid_contributive_money:
            if hasattr(self.paid_contributive_money, 'to_alipay_dict'):
                params['paid_contributive_money'] = self.paid_contributive_money.to_alipay_dict()
            else:
                params['paid_contributive_money'] = self.paid_contributive_money
        if self.paid_contributive_way:
            if hasattr(self.paid_contributive_way, 'to_alipay_dict'):
                params['paid_contributive_way'] = self.paid_contributive_way.to_alipay_dict()
            else:
                params['paid_contributive_way'] = self.paid_contributive_way
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
        if self.shareholder:
            if hasattr(self.shareholder, 'to_alipay_dict'):
                params['shareholder'] = self.shareholder.to_alipay_dict()
            else:
                params['shareholder'] = self.shareholder
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmepAnnualReportShareholderInfo()
        if 'paid_contributive_date' in d:
            o.paid_contributive_date = d['paid_contributive_date']
        if 'paid_contributive_money' in d:
            o.paid_contributive_money = d['paid_contributive_money']
        if 'paid_contributive_way' in d:
            o.paid_contributive_way = d['paid_contributive_way']
        if 'paid_in_contributive_date' in d:
            o.paid_in_contributive_date = d['paid_in_contributive_date']
        if 'paid_in_contributive_money' in d:
            o.paid_in_contributive_money = d['paid_in_contributive_money']
        if 'paid_in_contributive_way' in d:
            o.paid_in_contributive_way = d['paid_in_contributive_way']
        if 'shareholder' in d:
            o.shareholder = d['shareholder']
        return o


