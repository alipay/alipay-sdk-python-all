#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LineRepetitionVO(object):

    def __init__(self):
        self._city_code = None
        self._dt = None
        self._line_key = None
        self._repetition = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def dt(self):
        return self._dt

    @dt.setter
    def dt(self, value):
        self._dt = value
    @property
    def line_key(self):
        return self._line_key

    @line_key.setter
    def line_key(self, value):
        self._line_key = value
    @property
    def repetition(self):
        return self._repetition

    @repetition.setter
    def repetition(self, value):
        self._repetition = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.dt:
            if hasattr(self.dt, 'to_alipay_dict'):
                params['dt'] = self.dt.to_alipay_dict()
            else:
                params['dt'] = self.dt
        if self.line_key:
            if hasattr(self.line_key, 'to_alipay_dict'):
                params['line_key'] = self.line_key.to_alipay_dict()
            else:
                params['line_key'] = self.line_key
        if self.repetition:
            if hasattr(self.repetition, 'to_alipay_dict'):
                params['repetition'] = self.repetition.to_alipay_dict()
            else:
                params['repetition'] = self.repetition
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LineRepetitionVO()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'dt' in d:
            o.dt = d['dt']
        if 'line_key' in d:
            o.line_key = d['line_key']
        if 'repetition' in d:
            o.repetition = d['repetition']
        return o


