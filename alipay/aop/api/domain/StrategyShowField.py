#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StrategyShowField(object):

    def __init__(self):
        self._component_name = None
        self._field_code = None
        self._field_name = None

    @property
    def component_name(self):
        return self._component_name

    @component_name.setter
    def component_name(self, value):
        self._component_name = value
    @property
    def field_code(self):
        return self._field_code

    @field_code.setter
    def field_code(self, value):
        self._field_code = value
    @property
    def field_name(self):
        return self._field_name

    @field_name.setter
    def field_name(self, value):
        self._field_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.component_name:
            if hasattr(self.component_name, 'to_alipay_dict'):
                params['component_name'] = self.component_name.to_alipay_dict()
            else:
                params['component_name'] = self.component_name
        if self.field_code:
            if hasattr(self.field_code, 'to_alipay_dict'):
                params['field_code'] = self.field_code.to_alipay_dict()
            else:
                params['field_code'] = self.field_code
        if self.field_name:
            if hasattr(self.field_name, 'to_alipay_dict'):
                params['field_name'] = self.field_name.to_alipay_dict()
            else:
                params['field_name'] = self.field_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StrategyShowField()
        if 'component_name' in d:
            o.component_name = d['component_name']
        if 'field_code' in d:
            o.field_code = d['field_code']
        if 'field_name' in d:
            o.field_name = d['field_name']
        return o


