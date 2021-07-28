#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityLimitationDTO(object):

    def __init__(self):
        self._limit_num = None
        self._limit_type = None
        self._limited = None

    @property
    def limit_num(self):
        return self._limit_num

    @limit_num.setter
    def limit_num(self, value):
        self._limit_num = value
    @property
    def limit_type(self):
        return self._limit_type

    @limit_type.setter
    def limit_type(self, value):
        self._limit_type = value
    @property
    def limited(self):
        return self._limited

    @limited.setter
    def limited(self, value):
        self._limited = value


    def to_alipay_dict(self):
        params = dict()
        if self.limit_num:
            if hasattr(self.limit_num, 'to_alipay_dict'):
                params['limit_num'] = self.limit_num.to_alipay_dict()
            else:
                params['limit_num'] = self.limit_num
        if self.limit_type:
            if hasattr(self.limit_type, 'to_alipay_dict'):
                params['limit_type'] = self.limit_type.to_alipay_dict()
            else:
                params['limit_type'] = self.limit_type
        if self.limited:
            if hasattr(self.limited, 'to_alipay_dict'):
                params['limited'] = self.limited.to_alipay_dict()
            else:
                params['limited'] = self.limited
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityLimitationDTO()
        if 'limit_num' in d:
            o.limit_num = d['limit_num']
        if 'limit_type' in d:
            o.limit_type = d['limit_type']
        if 'limited' in d:
            o.limited = d['limited']
        return o


