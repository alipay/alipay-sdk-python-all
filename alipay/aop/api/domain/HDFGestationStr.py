#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HDFGestationStr(object):

    def __init__(self):
        self._add_time = None
        self._expected_date = None
        self._gestation_str = None
        self._is_gestation = None

    @property
    def add_time(self):
        return self._add_time

    @add_time.setter
    def add_time(self, value):
        self._add_time = value
    @property
    def expected_date(self):
        return self._expected_date

    @expected_date.setter
    def expected_date(self, value):
        self._expected_date = value
    @property
    def gestation_str(self):
        return self._gestation_str

    @gestation_str.setter
    def gestation_str(self, value):
        self._gestation_str = value
    @property
    def is_gestation(self):
        return self._is_gestation

    @is_gestation.setter
    def is_gestation(self, value):
        self._is_gestation = value


    def to_alipay_dict(self):
        params = dict()
        if self.add_time:
            if hasattr(self.add_time, 'to_alipay_dict'):
                params['add_time'] = self.add_time.to_alipay_dict()
            else:
                params['add_time'] = self.add_time
        if self.expected_date:
            if hasattr(self.expected_date, 'to_alipay_dict'):
                params['expected_date'] = self.expected_date.to_alipay_dict()
            else:
                params['expected_date'] = self.expected_date
        if self.gestation_str:
            if hasattr(self.gestation_str, 'to_alipay_dict'):
                params['gestation_str'] = self.gestation_str.to_alipay_dict()
            else:
                params['gestation_str'] = self.gestation_str
        if self.is_gestation:
            if hasattr(self.is_gestation, 'to_alipay_dict'):
                params['is_gestation'] = self.is_gestation.to_alipay_dict()
            else:
                params['is_gestation'] = self.is_gestation
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HDFGestationStr()
        if 'add_time' in d:
            o.add_time = d['add_time']
        if 'expected_date' in d:
            o.expected_date = d['expected_date']
        if 'gestation_str' in d:
            o.gestation_str = d['gestation_str']
        if 'is_gestation' in d:
            o.is_gestation = d['is_gestation']
        return o


