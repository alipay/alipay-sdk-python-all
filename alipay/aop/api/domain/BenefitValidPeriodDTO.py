#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitValidPeriodDTO(object):

    def __init__(self):
        self._active_seconds_after_receive = None
        self._active_time = None
        self._end_time = None
        self._expire_seconds_after_receive = None
        self._type = None

    @property
    def active_seconds_after_receive(self):
        return self._active_seconds_after_receive

    @active_seconds_after_receive.setter
    def active_seconds_after_receive(self, value):
        self._active_seconds_after_receive = value
    @property
    def active_time(self):
        return self._active_time

    @active_time.setter
    def active_time(self, value):
        self._active_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def expire_seconds_after_receive(self):
        return self._expire_seconds_after_receive

    @expire_seconds_after_receive.setter
    def expire_seconds_after_receive(self, value):
        self._expire_seconds_after_receive = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_seconds_after_receive:
            if hasattr(self.active_seconds_after_receive, 'to_alipay_dict'):
                params['active_seconds_after_receive'] = self.active_seconds_after_receive.to_alipay_dict()
            else:
                params['active_seconds_after_receive'] = self.active_seconds_after_receive
        if self.active_time:
            if hasattr(self.active_time, 'to_alipay_dict'):
                params['active_time'] = self.active_time.to_alipay_dict()
            else:
                params['active_time'] = self.active_time
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.expire_seconds_after_receive:
            if hasattr(self.expire_seconds_after_receive, 'to_alipay_dict'):
                params['expire_seconds_after_receive'] = self.expire_seconds_after_receive.to_alipay_dict()
            else:
                params['expire_seconds_after_receive'] = self.expire_seconds_after_receive
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitValidPeriodDTO()
        if 'active_seconds_after_receive' in d:
            o.active_seconds_after_receive = d['active_seconds_after_receive']
        if 'active_time' in d:
            o.active_time = d['active_time']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'expire_seconds_after_receive' in d:
            o.expire_seconds_after_receive = d['expire_seconds_after_receive']
        if 'type' in d:
            o.type = d['type']
        return o


