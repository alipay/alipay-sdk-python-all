#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScheduleInfo(object):

    def __init__(self):
        self._bitmap = None
        self._date = None

    @property
    def bitmap(self):
        return self._bitmap

    @bitmap.setter
    def bitmap(self, value):
        self._bitmap = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value


    def to_alipay_dict(self):
        params = dict()
        if self.bitmap:
            if hasattr(self.bitmap, 'to_alipay_dict'):
                params['bitmap'] = self.bitmap.to_alipay_dict()
            else:
                params['bitmap'] = self.bitmap
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScheduleInfo()
        if 'bitmap' in d:
            o.bitmap = d['bitmap']
        if 'date' in d:
            o.date = d['date']
        return o


