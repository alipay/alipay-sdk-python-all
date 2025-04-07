#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpuAttributeInfoVO(object):

    def __init__(self):
        self._attr_key = None
        self._attr_name = None
        self._attr_value = None
        self._attr_value_id = None

    @property
    def attr_key(self):
        return self._attr_key

    @attr_key.setter
    def attr_key(self, value):
        self._attr_key = value
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
    @property
    def attr_value_id(self):
        return self._attr_value_id

    @attr_value_id.setter
    def attr_value_id(self, value):
        self._attr_value_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.attr_key:
            if hasattr(self.attr_key, 'to_alipay_dict'):
                params['attr_key'] = self.attr_key.to_alipay_dict()
            else:
                params['attr_key'] = self.attr_key
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
        if self.attr_value_id:
            if hasattr(self.attr_value_id, 'to_alipay_dict'):
                params['attr_value_id'] = self.attr_value_id.to_alipay_dict()
            else:
                params['attr_value_id'] = self.attr_value_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpuAttributeInfoVO()
        if 'attr_key' in d:
            o.attr_key = d['attr_key']
        if 'attr_name' in d:
            o.attr_name = d['attr_name']
        if 'attr_value' in d:
            o.attr_value = d['attr_value']
        if 'attr_value_id' in d:
            o.attr_value_id = d['attr_value_id']
        return o


