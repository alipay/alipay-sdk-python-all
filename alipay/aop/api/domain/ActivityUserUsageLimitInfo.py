#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityUserUsageLimitInfo(object):

    def __init__(self):
        self._limit_count = None
        self._limit_type = None
        self._usage_rule_type = None
        self._usage_time_type = None

    @property
    def limit_count(self):
        return self._limit_count

    @limit_count.setter
    def limit_count(self, value):
        self._limit_count = value
    @property
    def limit_type(self):
        return self._limit_type

    @limit_type.setter
    def limit_type(self, value):
        self._limit_type = value
    @property
    def usage_rule_type(self):
        return self._usage_rule_type

    @usage_rule_type.setter
    def usage_rule_type(self, value):
        self._usage_rule_type = value
    @property
    def usage_time_type(self):
        return self._usage_time_type

    @usage_time_type.setter
    def usage_time_type(self, value):
        self._usage_time_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.limit_count:
            if hasattr(self.limit_count, 'to_alipay_dict'):
                params['limit_count'] = self.limit_count.to_alipay_dict()
            else:
                params['limit_count'] = self.limit_count
        if self.limit_type:
            if hasattr(self.limit_type, 'to_alipay_dict'):
                params['limit_type'] = self.limit_type.to_alipay_dict()
            else:
                params['limit_type'] = self.limit_type
        if self.usage_rule_type:
            if hasattr(self.usage_rule_type, 'to_alipay_dict'):
                params['usage_rule_type'] = self.usage_rule_type.to_alipay_dict()
            else:
                params['usage_rule_type'] = self.usage_rule_type
        if self.usage_time_type:
            if hasattr(self.usage_time_type, 'to_alipay_dict'):
                params['usage_time_type'] = self.usage_time_type.to_alipay_dict()
            else:
                params['usage_time_type'] = self.usage_time_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityUserUsageLimitInfo()
        if 'limit_count' in d:
            o.limit_count = d['limit_count']
        if 'limit_type' in d:
            o.limit_type = d['limit_type']
        if 'usage_rule_type' in d:
            o.usage_rule_type = d['usage_rule_type']
        if 'usage_time_type' in d:
            o.usage_time_type = d['usage_time_type']
        return o


