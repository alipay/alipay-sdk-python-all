#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalHmDailySleepRecord(object):

    def __init__(self):
        self._data_type = None
        self._sleep_date = None
        self._sleepdata = None

    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def sleep_date(self):
        return self._sleep_date

    @sleep_date.setter
    def sleep_date(self, value):
        self._sleep_date = value
    @property
    def sleepdata(self):
        return self._sleepdata

    @sleepdata.setter
    def sleepdata(self, value):
        self._sleepdata = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.sleep_date:
            if hasattr(self.sleep_date, 'to_alipay_dict'):
                params['sleep_date'] = self.sleep_date.to_alipay_dict()
            else:
                params['sleep_date'] = self.sleep_date
        if self.sleepdata:
            if hasattr(self.sleepdata, 'to_alipay_dict'):
                params['sleepdata'] = self.sleepdata.to_alipay_dict()
            else:
                params['sleepdata'] = self.sleepdata
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalHmDailySleepRecord()
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'sleep_date' in d:
            o.sleep_date = d['sleep_date']
        if 'sleepdata' in d:
            o.sleepdata = d['sleepdata']
        return o


