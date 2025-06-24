#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleQcMetadata(object):

    def __init__(self):
        self._attr_name = None
        self._attr_value = None

    @property
    def attr_name(self):
        return self._attr_name

    @attr_name.setter
    def attr_name(self, value):
        self._attr_name = value
    @property
    def attr_value(self):
        return self._attr_value

    @attr_value.setter
    def attr_value(self, value):
        self._attr_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.attr_name:
            if hasattr(self.attr_name, 'to_alipay_dict'):
                params['attr_name'] = self.attr_name.to_alipay_dict()
            else:
                params['attr_name'] = self.attr_name
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
        o = RecycleQcMetadata()
        if 'attr_name' in d:
            o.attr_name = d['attr_name']
        if 'attr_value' in d:
            o.attr_value = d['attr_value']
        return o


