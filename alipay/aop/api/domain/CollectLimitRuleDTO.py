#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CollectLimitRuleDTO(object):

    def __init__(self):
        self._count = None
        self._limit_time_type = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def limit_time_type(self):
        return self._limit_time_type

    @limit_time_type.setter
    def limit_time_type(self, value):
        self._limit_time_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.limit_time_type:
            if hasattr(self.limit_time_type, 'to_alipay_dict'):
                params['limit_time_type'] = self.limit_time_type.to_alipay_dict()
            else:
                params['limit_time_type'] = self.limit_time_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CollectLimitRuleDTO()
        if 'count' in d:
            o.count = d['count']
        if 'limit_time_type' in d:
            o.limit_time_type = d['limit_time_type']
        return o


