#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LoadInfoNode(object):

    def __init__(self):
        self._end_time = None
        self._load = None
        self._start_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def load(self):
        return self._load

    @load.setter
    def load(self, value):
        self._load = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.load:
            if hasattr(self.load, 'to_alipay_dict'):
                params['load'] = self.load.to_alipay_dict()
            else:
                params['load'] = self.load
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LoadInfoNode()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'load' in d:
            o.load = d['load']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


