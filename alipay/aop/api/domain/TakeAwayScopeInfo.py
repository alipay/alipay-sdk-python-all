#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TakeAwayScopeInfo(object):

    def __init__(self):
        self._circular_area = None
        self._code = None
        self._min_price = None
        self._polygon_area = None
        self._shipping_area = None
        self._type = None

    @property
    def circular_area(self):
        return self._circular_area

    @circular_area.setter
    def circular_area(self, value):
        self._circular_area = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def min_price(self):
        return self._min_price

    @min_price.setter
    def min_price(self, value):
        self._min_price = value
    @property
    def polygon_area(self):
        return self._polygon_area

    @polygon_area.setter
    def polygon_area(self, value):
        if isinstance(value, list):
            self._polygon_area = list()
            for i in value:
                self._polygon_area.append(i)
    @property
    def shipping_area(self):
        return self._shipping_area

    @shipping_area.setter
    def shipping_area(self, value):
        self._shipping_area = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.circular_area:
            if hasattr(self.circular_area, 'to_alipay_dict'):
                params['circular_area'] = self.circular_area.to_alipay_dict()
            else:
                params['circular_area'] = self.circular_area
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.min_price:
            if hasattr(self.min_price, 'to_alipay_dict'):
                params['min_price'] = self.min_price.to_alipay_dict()
            else:
                params['min_price'] = self.min_price
        if self.polygon_area:
            if isinstance(self.polygon_area, list):
                for i in range(0, len(self.polygon_area)):
                    element = self.polygon_area[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.polygon_area[i] = element.to_alipay_dict()
            if hasattr(self.polygon_area, 'to_alipay_dict'):
                params['polygon_area'] = self.polygon_area.to_alipay_dict()
            else:
                params['polygon_area'] = self.polygon_area
        if self.shipping_area:
            if hasattr(self.shipping_area, 'to_alipay_dict'):
                params['shipping_area'] = self.shipping_area.to_alipay_dict()
            else:
                params['shipping_area'] = self.shipping_area
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TakeAwayScopeInfo()
        if 'circular_area' in d:
            o.circular_area = d['circular_area']
        if 'code' in d:
            o.code = d['code']
        if 'min_price' in d:
            o.min_price = d['min_price']
        if 'polygon_area' in d:
            o.polygon_area = d['polygon_area']
        if 'shipping_area' in d:
            o.shipping_area = d['shipping_area']
        if 'type' in d:
            o.type = d['type']
        return o


