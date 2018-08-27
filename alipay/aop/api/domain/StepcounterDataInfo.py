#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StepcounterDataInfo(object):

    def __init__(self):
        self._count = None
        self._count_date = None
        self._time_zone = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def count_date(self):
        return self._count_date

    @count_date.setter
    def count_date(self, value):
        self._count_date = value
    @property
    def time_zone(self):
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        self._time_zone = value


    def to_alipay_dict(self):
        params = dict()
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.count_date:
            if hasattr(self.count_date, 'to_alipay_dict'):
                params['count_date'] = self.count_date.to_alipay_dict()
            else:
                params['count_date'] = self.count_date
        if self.time_zone:
            if hasattr(self.time_zone, 'to_alipay_dict'):
                params['time_zone'] = self.time_zone.to_alipay_dict()
            else:
                params['time_zone'] = self.time_zone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StepcounterDataInfo()
        if 'count' in d:
            o.count = d['count']
        if 'count_date' in d:
            o.count_date = d['count_date']
        if 'time_zone' in d:
            o.time_zone = d['time_zone']
        return o


