#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IgAuthQuota(object):

    def __init__(self):
        self._quota_count = None
        self._range_type = None

    @property
    def quota_count(self):
        return self._quota_count

    @quota_count.setter
    def quota_count(self, value):
        self._quota_count = value
    @property
    def range_type(self):
        return self._range_type

    @range_type.setter
    def range_type(self, value):
        self._range_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.quota_count:
            if hasattr(self.quota_count, 'to_alipay_dict'):
                params['quota_count'] = self.quota_count.to_alipay_dict()
            else:
                params['quota_count'] = self.quota_count
        if self.range_type:
            if hasattr(self.range_type, 'to_alipay_dict'):
                params['range_type'] = self.range_type.to_alipay_dict()
            else:
                params['range_type'] = self.range_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IgAuthQuota()
        if 'quota_count' in d:
            o.quota_count = d['quota_count']
        if 'range_type' in d:
            o.range_type = d['range_type']
        return o


