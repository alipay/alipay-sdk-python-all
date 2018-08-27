#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LendingRecords(object):

    def __init__(self):
        self._date = None
        self._remark = None
        self._total_amount = None

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
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LendingRecords()
        if 'date' in d:
            o.date = d['date']
        if 'remark' in d:
            o.remark = d['remark']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


