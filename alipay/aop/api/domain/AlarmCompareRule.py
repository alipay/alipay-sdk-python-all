#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlarmCompareRule(object):

    def __init__(self):
        self._operate_type = None
        self._operate_value = None

    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def operate_value(self):
        return self._operate_value

    @operate_value.setter
    def operate_value(self, value):
        self._operate_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.operate_value:
            if hasattr(self.operate_value, 'to_alipay_dict'):
                params['operate_value'] = self.operate_value.to_alipay_dict()
            else:
                params['operate_value'] = self.operate_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlarmCompareRule()
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'operate_value' in d:
            o.operate_value = d['operate_value']
        return o


