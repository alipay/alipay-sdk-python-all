#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpiVoiceCallback(object):

    def __init__(self):
        self._call_id = None
        self._callee = None
        self._duration = None
        self._end_time = None
        self._out_id = None
        self._start_time = None
        self._status_code = None

    @property
    def call_id(self):
        return self._call_id

    @call_id.setter
    def call_id(self, value):
        self._call_id = value
    @property
    def callee(self):
        return self._callee

    @callee.setter
    def callee(self, value):
        self._callee = value
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def out_id(self):
        return self._out_id

    @out_id.setter
    def out_id(self, value):
        self._out_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.call_id:
            if hasattr(self.call_id, 'to_alipay_dict'):
                params['call_id'] = self.call_id.to_alipay_dict()
            else:
                params['call_id'] = self.call_id
        if self.callee:
            if hasattr(self.callee, 'to_alipay_dict'):
                params['callee'] = self.callee.to_alipay_dict()
            else:
                params['callee'] = self.callee
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.out_id:
            if hasattr(self.out_id, 'to_alipay_dict'):
                params['out_id'] = self.out_id.to_alipay_dict()
            else:
                params['out_id'] = self.out_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status_code:
            if hasattr(self.status_code, 'to_alipay_dict'):
                params['status_code'] = self.status_code.to_alipay_dict()
            else:
                params['status_code'] = self.status_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpiVoiceCallback()
        if 'call_id' in d:
            o.call_id = d['call_id']
        if 'callee' in d:
            o.callee = d['callee']
        if 'duration' in d:
            o.duration = d['duration']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'out_id' in d:
            o.out_id = d['out_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status_code' in d:
            o.status_code = d['status_code']
        return o


