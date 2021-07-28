#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HealthServiceItemSkuPropertyDTO(object):

    def __init__(self):
        self._sku_property_key_display = None
        self._sku_property_value_display = None

    @property
    def sku_property_key_display(self):
        return self._sku_property_key_display

    @sku_property_key_display.setter
    def sku_property_key_display(self, value):
        self._sku_property_key_display = value
    @property
    def sku_property_value_display(self):
        return self._sku_property_value_display

    @sku_property_value_display.setter
    def sku_property_value_display(self, value):
        self._sku_property_value_display = value


    def to_alipay_dict(self):
        params = dict()
        if self.sku_property_key_display:
            if hasattr(self.sku_property_key_display, 'to_alipay_dict'):
                params['sku_property_key_display'] = self.sku_property_key_display.to_alipay_dict()
            else:
                params['sku_property_key_display'] = self.sku_property_key_display
        if self.sku_property_value_display:
            if hasattr(self.sku_property_value_display, 'to_alipay_dict'):
                params['sku_property_value_display'] = self.sku_property_value_display.to_alipay_dict()
            else:
                params['sku_property_value_display'] = self.sku_property_value_display
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HealthServiceItemSkuPropertyDTO()
        if 'sku_property_key_display' in d:
            o.sku_property_key_display = d['sku_property_key_display']
        if 'sku_property_value_display' in d:
            o.sku_property_value_display = d['sku_property_value_display']
        return o


