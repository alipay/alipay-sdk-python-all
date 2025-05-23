#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ComplexBusinessTimePeriod(object):

    def __init__(self):
        self._close_time = None
        self._open_time = None

    @property
    def close_time(self):
        return self._close_time

    @close_time.setter
    def close_time(self, value):
        self._close_time = value
    @property
    def open_time(self):
        return self._open_time

    @open_time.setter
    def open_time(self, value):
        self._open_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.close_time:
            if hasattr(self.close_time, 'to_alipay_dict'):
                params['close_time'] = self.close_time.to_alipay_dict()
            else:
                params['close_time'] = self.close_time
        if self.open_time:
            if hasattr(self.open_time, 'to_alipay_dict'):
                params['open_time'] = self.open_time.to_alipay_dict()
            else:
                params['open_time'] = self.open_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ComplexBusinessTimePeriod()
        if 'close_time' in d:
            o.close_time = d['close_time']
        if 'open_time' in d:
            o.open_time = d['open_time']
        return o


