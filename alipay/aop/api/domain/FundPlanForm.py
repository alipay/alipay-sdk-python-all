#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FundPlanForm(object):

    def __init__(self):
        self._amount = None
        self._calendar_type = None
        self._date = None
        self._remark = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def calendar_type(self):
        return self._calendar_type

    @calendar_type.setter
    def calendar_type(self, value):
        self._calendar_type = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.calendar_type:
            if hasattr(self.calendar_type, 'to_alipay_dict'):
                params['calendar_type'] = self.calendar_type.to_alipay_dict()
            else:
                params['calendar_type'] = self.calendar_type
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FundPlanForm()
        if 'amount' in d:
            o.amount = d['amount']
        if 'calendar_type' in d:
            o.calendar_type = d['calendar_type']
        if 'date' in d:
            o.date = d['date']
        if 'remark' in d:
            o.remark = d['remark']
        return o


