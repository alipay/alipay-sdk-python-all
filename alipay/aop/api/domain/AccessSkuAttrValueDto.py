#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccessSkuAttrValueDto(object):

    def __init__(self):
        self._attr_name = None
        self._attr_value_name = None

    @property
    def attr_name(self):
        return self._attr_name

    @attr_name.setter
    def attr_name(self, value):
        self._attr_name = value
    @property
    def attr_value_name(self):
        return self._attr_value_name

    @attr_value_name.setter
    def attr_value_name(self, value):
        self._attr_value_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.attr_name:
            if hasattr(self.attr_name, 'to_alipay_dict'):
                params['attr_name'] = self.attr_name.to_alipay_dict()
            else:
                params['attr_name'] = self.attr_name
        if self.attr_value_name:
            if hasattr(self.attr_value_name, 'to_alipay_dict'):
                params['attr_value_name'] = self.attr_value_name.to_alipay_dict()
            else:
                params['attr_value_name'] = self.attr_value_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccessSkuAttrValueDto()
        if 'attr_name' in d:
            o.attr_name = d['attr_name']
        if 'attr_value_name' in d:
            o.attr_value_name = d['attr_value_name']
        return o


