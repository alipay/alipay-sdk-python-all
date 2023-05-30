#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DspCreativeElement(object):

    def __init__(self):
        self._attr_key = None
        self._attr_value = None

    @property
    def attr_key(self):
        return self._attr_key

    @attr_key.setter
    def attr_key(self, value):
        self._attr_key = value
    @property
    def attr_value(self):
        return self._attr_value

    @attr_value.setter
    def attr_value(self, value):
        if isinstance(value, list):
            self._attr_value = list()
            for i in value:
                self._attr_value.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.attr_key:
            if hasattr(self.attr_key, 'to_alipay_dict'):
                params['attr_key'] = self.attr_key.to_alipay_dict()
            else:
                params['attr_key'] = self.attr_key
        if self.attr_value:
            if isinstance(self.attr_value, list):
                for i in range(0, len(self.attr_value)):
                    element = self.attr_value[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attr_value[i] = element.to_alipay_dict()
            if hasattr(self.attr_value, 'to_alipay_dict'):
                params['attr_value'] = self.attr_value.to_alipay_dict()
            else:
                params['attr_value'] = self.attr_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DspCreativeElement()
        if 'attr_key' in d:
            o.attr_key = d['attr_key']
        if 'attr_value' in d:
            o.attr_value = d['attr_value']
        return o


