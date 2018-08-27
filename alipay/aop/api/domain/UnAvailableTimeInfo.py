#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UnAvailableTimeInfo(object):

    def __init__(self):
        self._from_date = None
        self._to_date = None

    @property
    def from_date(self):
        return self._from_date

    @from_date.setter
    def from_date(self, value):
        self._from_date = value
    @property
    def to_date(self):
        return self._to_date

    @to_date.setter
    def to_date(self, value):
        self._to_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.from_date:
            if hasattr(self.from_date, 'to_alipay_dict'):
                params['from_date'] = self.from_date.to_alipay_dict()
            else:
                params['from_date'] = self.from_date
        if self.to_date:
            if hasattr(self.to_date, 'to_alipay_dict'):
                params['to_date'] = self.to_date.to_alipay_dict()
            else:
                params['to_date'] = self.to_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UnAvailableTimeInfo()
        if 'from_date' in d:
            o.from_date = d['from_date']
        if 'to_date' in d:
            o.to_date = d['to_date']
        return o


