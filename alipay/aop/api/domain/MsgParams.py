#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MsgParams(object):

    def __init__(self):
        self._bill_amount = None
        self._company_name = None
        self._expire_days = None
        self._repay_date = None

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def expire_days(self):
        return self._expire_days

    @expire_days.setter
    def expire_days(self, value):
        self._expire_days = value
    @property
    def repay_date(self):
        return self._repay_date

    @repay_date.setter
    def repay_date(self, value):
        self._repay_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.expire_days:
            if hasattr(self.expire_days, 'to_alipay_dict'):
                params['expire_days'] = self.expire_days.to_alipay_dict()
            else:
                params['expire_days'] = self.expire_days
        if self.repay_date:
            if hasattr(self.repay_date, 'to_alipay_dict'):
                params['repay_date'] = self.repay_date.to_alipay_dict()
            else:
                params['repay_date'] = self.repay_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MsgParams()
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'expire_days' in d:
            o.expire_days = d['expire_days']
        if 'repay_date' in d:
            o.repay_date = d['repay_date']
        return o


