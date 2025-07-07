#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MallSkuAttrValue(object):

    def __init__(self):
        self._attr_en_name = None
        self._attr_en_value = None
        self._attr_id = None
        self._attr_name = None
        self._attr_value = None
        self._attr_value_id = None
        self._sku_id = None

    @property
    def attr_en_name(self):
        return self._attr_en_name

    @attr_en_name.setter
    def attr_en_name(self, value):
        self._attr_en_name = value
    @property
    def attr_en_value(self):
        return self._attr_en_value

    @attr_en_value.setter
    def attr_en_value(self, value):
        self._attr_en_value = value
    @property
    def attr_id(self):
        return self._attr_id

    @attr_id.setter
    def attr_id(self, value):
        self._attr_id = value
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
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.attr_en_name:
            if hasattr(self.attr_en_name, 'to_alipay_dict'):
                params['attr_en_name'] = self.attr_en_name.to_alipay_dict()
            else:
                params['attr_en_name'] = self.attr_en_name
        if self.attr_en_value:
            if hasattr(self.attr_en_value, 'to_alipay_dict'):
                params['attr_en_value'] = self.attr_en_value.to_alipay_dict()
            else:
                params['attr_en_value'] = self.attr_en_value
        if self.attr_id:
            if hasattr(self.attr_id, 'to_alipay_dict'):
                params['attr_id'] = self.attr_id.to_alipay_dict()
            else:
                params['attr_id'] = self.attr_id
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
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MallSkuAttrValue()
        if 'attr_en_name' in d:
            o.attr_en_name = d['attr_en_name']
        if 'attr_en_value' in d:
            o.attr_en_value = d['attr_en_value']
        if 'attr_id' in d:
            o.attr_id = d['attr_id']
        if 'attr_name' in d:
            o.attr_name = d['attr_name']
        if 'attr_value' in d:
            o.attr_value = d['attr_value']
        if 'attr_value_id' in d:
            o.attr_value_id = d['attr_value_id']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


