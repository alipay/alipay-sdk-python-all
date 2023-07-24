#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DynamicAwardConfigDataDto(object):

    def __init__(self):
        self._count_limit = None
        self._dynamic_award_count = None

    @property
    def count_limit(self):
        return self._count_limit

    @count_limit.setter
    def count_limit(self, value):
        self._count_limit = value
    @property
    def dynamic_award_count(self):
        return self._dynamic_award_count

    @dynamic_award_count.setter
    def dynamic_award_count(self, value):
        self._dynamic_award_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.count_limit:
            if hasattr(self.count_limit, 'to_alipay_dict'):
                params['count_limit'] = self.count_limit.to_alipay_dict()
            else:
                params['count_limit'] = self.count_limit
        if self.dynamic_award_count:
            if hasattr(self.dynamic_award_count, 'to_alipay_dict'):
                params['dynamic_award_count'] = self.dynamic_award_count.to_alipay_dict()
            else:
                params['dynamic_award_count'] = self.dynamic_award_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DynamicAwardConfigDataDto()
        if 'count_limit' in d:
            o.count_limit = d['count_limit']
        if 'dynamic_award_count' in d:
            o.dynamic_award_count = d['dynamic_award_count']
        return o


