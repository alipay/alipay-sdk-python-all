#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MsgDynamicData(object):

    def __init__(self):
        self._dynamic_type = None
        self._dynamic_value = None

    @property
    def dynamic_type(self):
        return self._dynamic_type

    @dynamic_type.setter
    def dynamic_type(self, value):
        self._dynamic_type = value
    @property
    def dynamic_value(self):
        return self._dynamic_value

    @dynamic_value.setter
    def dynamic_value(self, value):
        self._dynamic_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.dynamic_type:
            if hasattr(self.dynamic_type, 'to_alipay_dict'):
                params['dynamic_type'] = self.dynamic_type.to_alipay_dict()
            else:
                params['dynamic_type'] = self.dynamic_type
        if self.dynamic_value:
            if hasattr(self.dynamic_value, 'to_alipay_dict'):
                params['dynamic_value'] = self.dynamic_value.to_alipay_dict()
            else:
                params['dynamic_value'] = self.dynamic_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MsgDynamicData()
        if 'dynamic_type' in d:
            o.dynamic_type = d['dynamic_type']
        if 'dynamic_value' in d:
            o.dynamic_value = d['dynamic_value']
        return o


