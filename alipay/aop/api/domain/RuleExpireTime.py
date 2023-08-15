#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RuleExpireTime(object):

    def __init__(self):
        self._effect_time = None
        self._expire_time = None
        self._expire_type = None

    @property
    def effect_time(self):
        return self._effect_time

    @effect_time.setter
    def effect_time(self, value):
        self._effect_time = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def expire_type(self):
        return self._expire_type

    @expire_type.setter
    def expire_type(self, value):
        self._expire_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.effect_time:
            if hasattr(self.effect_time, 'to_alipay_dict'):
                params['effect_time'] = self.effect_time.to_alipay_dict()
            else:
                params['effect_time'] = self.effect_time
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.expire_type:
            if hasattr(self.expire_type, 'to_alipay_dict'):
                params['expire_type'] = self.expire_type.to_alipay_dict()
            else:
                params['expire_type'] = self.expire_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RuleExpireTime()
        if 'effect_time' in d:
            o.effect_time = d['effect_time']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'expire_type' in d:
            o.expire_type = d['expire_type']
        return o


