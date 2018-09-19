#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReportCondition(object):

    def __init__(self):
        self._key = None
        self._operate = None

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def operate(self):
        return self._operate

    @operate.setter
    def operate(self, value):
        self._operate = value


    def to_alipay_dict(self):
        params = dict()
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.operate:
            if hasattr(self.operate, 'to_alipay_dict'):
                params['operate'] = self.operate.to_alipay_dict()
            else:
                params['operate'] = self.operate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReportCondition()
        if 'key' in d:
            o.key = d['key']
        if 'operate' in d:
            o.operate = d['operate']
        return o


