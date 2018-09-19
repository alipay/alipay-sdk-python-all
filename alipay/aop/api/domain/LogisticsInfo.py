#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LogisticsInfo(object):

    def __init__(self):
        self._logistics_code = None
        self._logistics_name = None
        self._logistics_no = None

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
    @property
    def logistics_no(self):
        return self._logistics_no

    @logistics_no.setter
    def logistics_no(self, value):
        self._logistics_no = value


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
        if self.logistics_no:
            if hasattr(self.logistics_no, 'to_alipay_dict'):
                params['logistics_no'] = self.logistics_no.to_alipay_dict()
            else:
                params['logistics_no'] = self.logistics_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsInfo()
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'logistics_name' in d:
            o.logistics_name = d['logistics_name']
        if 'logistics_no' in d:
            o.logistics_no = d['logistics_no']
        return o


