#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FeatureVO(object):

    def __init__(self):
        self._congestion_rate = None
        self._real_time = None
        self._start_end = None

    @property
    def congestion_rate(self):
        return self._congestion_rate

    @congestion_rate.setter
    def congestion_rate(self, value):
        self._congestion_rate = value
    @property
    def real_time(self):
        return self._real_time

    @real_time.setter
    def real_time(self, value):
        self._real_time = value
    @property
    def start_end(self):
        return self._start_end

    @start_end.setter
    def start_end(self, value):
        self._start_end = value


    def to_alipay_dict(self):
        params = dict()
        if self.congestion_rate:
            if hasattr(self.congestion_rate, 'to_alipay_dict'):
                params['congestion_rate'] = self.congestion_rate.to_alipay_dict()
            else:
                params['congestion_rate'] = self.congestion_rate
        if self.real_time:
            if hasattr(self.real_time, 'to_alipay_dict'):
                params['real_time'] = self.real_time.to_alipay_dict()
            else:
                params['real_time'] = self.real_time
        if self.start_end:
            if hasattr(self.start_end, 'to_alipay_dict'):
                params['start_end'] = self.start_end.to_alipay_dict()
            else:
                params['start_end'] = self.start_end
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FeatureVO()
        if 'congestion_rate' in d:
            o.congestion_rate = d['congestion_rate']
        if 'real_time' in d:
            o.real_time = d['real_time']
        if 'start_end' in d:
            o.start_end = d['start_end']
        return o


