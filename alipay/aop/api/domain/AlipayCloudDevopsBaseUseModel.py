#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudDevopsBaseUseModel(object):

    def __init__(self):
        self._condition = None
        self._service_code = None
        self._sub_code = None
        self._sub_name = None

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        self._condition = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def sub_code(self):
        return self._sub_code

    @sub_code.setter
    def sub_code(self, value):
        self._sub_code = value
    @property
    def sub_name(self):
        return self._sub_name

    @sub_name.setter
    def sub_name(self, value):
        self._sub_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.condition:
            if hasattr(self.condition, 'to_alipay_dict'):
                params['condition'] = self.condition.to_alipay_dict()
            else:
                params['condition'] = self.condition
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.sub_code:
            if hasattr(self.sub_code, 'to_alipay_dict'):
                params['sub_code'] = self.sub_code.to_alipay_dict()
            else:
                params['sub_code'] = self.sub_code
        if self.sub_name:
            if hasattr(self.sub_name, 'to_alipay_dict'):
                params['sub_name'] = self.sub_name.to_alipay_dict()
            else:
                params['sub_name'] = self.sub_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudDevopsBaseUseModel()
        if 'condition' in d:
            o.condition = d['condition']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'sub_code' in d:
            o.sub_code = d['sub_code']
        if 'sub_name' in d:
            o.sub_name = d['sub_name']
        return o


