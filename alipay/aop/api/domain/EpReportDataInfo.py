#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpReportDataInfo(object):

    def __init__(self):
        self._biz_type = None
        self._biz_value = None
        self._status_code = None
        self._value_type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def biz_value(self):
        return self._biz_value

    @biz_value.setter
    def biz_value(self, value):
        self._biz_value = value
    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value
    @property
    def value_type(self):
        return self._value_type

    @value_type.setter
    def value_type(self, value):
        self._value_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.biz_value:
            if hasattr(self.biz_value, 'to_alipay_dict'):
                params['biz_value'] = self.biz_value.to_alipay_dict()
            else:
                params['biz_value'] = self.biz_value
        if self.status_code:
            if hasattr(self.status_code, 'to_alipay_dict'):
                params['status_code'] = self.status_code.to_alipay_dict()
            else:
                params['status_code'] = self.status_code
        if self.value_type:
            if hasattr(self.value_type, 'to_alipay_dict'):
                params['value_type'] = self.value_type.to_alipay_dict()
            else:
                params['value_type'] = self.value_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpReportDataInfo()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'biz_value' in d:
            o.biz_value = d['biz_value']
        if 'status_code' in d:
            o.status_code = d['status_code']
        if 'value_type' in d:
            o.value_type = d['value_type']
        return o


