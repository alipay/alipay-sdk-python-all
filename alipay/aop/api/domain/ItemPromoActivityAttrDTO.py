#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemPromoActivityAttrDTO(object):

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
        self._attr_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.attr_key:
            if hasattr(self.attr_key, 'to_alipay_dict'):
                params['attr_key'] = self.attr_key.to_alipay_dict()
            else:
                params['attr_key'] = self.attr_key
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
        o = ItemPromoActivityAttrDTO()
        if 'attr_key' in d:
            o.attr_key = d['attr_key']
        if 'attr_value' in d:
            o.attr_value = d['attr_value']
        return o


