#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LogisticsDetail(object):

    def __init__(self):
        self._logistics_type = None

    @property
    def logistics_type(self):
        return self._logistics_type

    @logistics_type.setter
    def logistics_type(self, value):
        self._logistics_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_type:
            if hasattr(self.logistics_type, 'to_alipay_dict'):
                params['logistics_type'] = self.logistics_type.to_alipay_dict()
            else:
                params['logistics_type'] = self.logistics_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsDetail()
        if 'logistics_type' in d:
            o.logistics_type = d['logistics_type']
        return o


