#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleSkuAttrDTO(object):

    def __init__(self):
        self._attr_code = None
        self._attr_value = None

    @property
    def attr_code(self):
        return self._attr_code

    @attr_code.setter
    def attr_code(self, value):
        self._attr_code = value
    @property
    def attr_value(self):
        return self._attr_value

    @attr_value.setter
    def attr_value(self, value):
        self._attr_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.attr_code:
            if hasattr(self.attr_code, 'to_alipay_dict'):
                params['attr_code'] = self.attr_code.to_alipay_dict()
            else:
                params['attr_code'] = self.attr_code
        if self.attr_value:
            if hasattr(self.attr_value, 'to_alipay_dict'):
                params['attr_value'] = self.attr_value.to_alipay_dict()
            else:
                params['attr_value'] = self.attr_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleSkuAttrDTO()
        if 'attr_code' in d:
            o.attr_code = d['attr_code']
        if 'attr_value' in d:
            o.attr_value = d['attr_value']
        return o


