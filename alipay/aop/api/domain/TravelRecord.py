#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TravelRecord(object):

    def __init__(self):
        self._bus_exist = None
        self._date = None
        self._metro_exist = None

    @property
    def bus_exist(self):
        return self._bus_exist

    @bus_exist.setter
    def bus_exist(self, value):
        self._bus_exist = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def metro_exist(self):
        return self._metro_exist

    @metro_exist.setter
    def metro_exist(self, value):
        self._metro_exist = value


    def to_alipay_dict(self):
        params = dict()
        if self.bus_exist:
            if hasattr(self.bus_exist, 'to_alipay_dict'):
                params['bus_exist'] = self.bus_exist.to_alipay_dict()
            else:
                params['bus_exist'] = self.bus_exist
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.metro_exist:
            if hasattr(self.metro_exist, 'to_alipay_dict'):
                params['metro_exist'] = self.metro_exist.to_alipay_dict()
            else:
                params['metro_exist'] = self.metro_exist
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TravelRecord()
        if 'bus_exist' in d:
            o.bus_exist = d['bus_exist']
        if 'date' in d:
            o.date = d['date']
        if 'metro_exist' in d:
            o.metro_exist = d['metro_exist']
        return o


