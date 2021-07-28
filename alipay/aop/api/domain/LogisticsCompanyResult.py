#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LogisticsCompanyResult(object):

    def __init__(self):
        self._logistics_code = None
        self._logistics_name = None

    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def logistics_name(self):
        return self._logistics_name

    @logistics_name.setter
    def logistics_name(self, value):
        self._logistics_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.logistics_name:
            if hasattr(self.logistics_name, 'to_alipay_dict'):
                params['logistics_name'] = self.logistics_name.to_alipay_dict()
            else:
                params['logistics_name'] = self.logistics_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsCompanyResult()
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'logistics_name' in d:
            o.logistics_name = d['logistics_name']
        return o


