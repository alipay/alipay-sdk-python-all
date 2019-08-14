#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CloudbusAvaliableItem(object):

    def __init__(self):
        self._city_code = None
        self._end_date = None
        self._max_size = None
        self._start_date = None
        self._status = None
        self._used_size = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def max_size(self):
        return self._max_size

    @max_size.setter
    def max_size(self, value):
        self._max_size = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def used_size(self):
        return self._used_size

    @used_size.setter
    def used_size(self, value):
        self._used_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.max_size:
            if hasattr(self.max_size, 'to_alipay_dict'):
                params['max_size'] = self.max_size.to_alipay_dict()
            else:
                params['max_size'] = self.max_size
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.used_size:
            if hasattr(self.used_size, 'to_alipay_dict'):
                params['used_size'] = self.used_size.to_alipay_dict()
            else:
                params['used_size'] = self.used_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CloudbusAvaliableItem()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'max_size' in d:
            o.max_size = d['max_size']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'status' in d:
            o.status = d['status']
        if 'used_size' in d:
            o.used_size = d['used_size']
        return o


