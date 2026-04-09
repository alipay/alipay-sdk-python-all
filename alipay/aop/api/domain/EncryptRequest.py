#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EncryptRequest(object):

    def __init__(self):
        self._encrypted = None
        self._time = None

    @property
    def encrypted(self):
        return self._encrypted

    @encrypted.setter
    def encrypted(self, value):
        self._encrypted = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value


    def to_alipay_dict(self):
        params = dict()
        if self.encrypted:
            if hasattr(self.encrypted, 'to_alipay_dict'):
                params['encrypted'] = self.encrypted.to_alipay_dict()
            else:
                params['encrypted'] = self.encrypted
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EncryptRequest()
        if 'encrypted' in d:
            o.encrypted = d['encrypted']
        if 'time' in d:
            o.time = d['time']
        return o


