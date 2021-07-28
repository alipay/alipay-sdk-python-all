#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GoodsInfoIstd(object):

    def __init__(self):
        self._delivery_info = None
        self._first_class = None
        self._height = None
        self._length = None
        self._pickup_info = None
        self._price = None
        self._second_class = None
        self._weight = None
        self._width = None

    @property
    def delivery_info(self):
        return self._delivery_info

    @delivery_info.setter
    def delivery_info(self, value):
        self._delivery_info = value
    @property
    def first_class(self):
        return self._first_class

    @first_class.setter
    def first_class(self, value):
        self._first_class = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value
    @property
    def pickup_info(self):
        return self._pickup_info

    @pickup_info.setter
    def pickup_info(self, value):
        self._pickup_info = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def second_class(self):
        return self._second_class

    @second_class.setter
    def second_class(self, value):
        self._second_class = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_info:
            if hasattr(self.delivery_info, 'to_alipay_dict'):
                params['delivery_info'] = self.delivery_info.to_alipay_dict()
            else:
                params['delivery_info'] = self.delivery_info
        if self.first_class:
            if hasattr(self.first_class, 'to_alipay_dict'):
                params['first_class'] = self.first_class.to_alipay_dict()
            else:
                params['first_class'] = self.first_class
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.length:
            if hasattr(self.length, 'to_alipay_dict'):
                params['length'] = self.length.to_alipay_dict()
            else:
                params['length'] = self.length
        if self.pickup_info:
            if hasattr(self.pickup_info, 'to_alipay_dict'):
                params['pickup_info'] = self.pickup_info.to_alipay_dict()
            else:
                params['pickup_info'] = self.pickup_info
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.second_class:
            if hasattr(self.second_class, 'to_alipay_dict'):
                params['second_class'] = self.second_class.to_alipay_dict()
            else:
                params['second_class'] = self.second_class
        if self.weight:
            if hasattr(self.weight, 'to_alipay_dict'):
                params['weight'] = self.weight.to_alipay_dict()
            else:
                params['weight'] = self.weight
        if self.width:
            if hasattr(self.width, 'to_alipay_dict'):
                params['width'] = self.width.to_alipay_dict()
            else:
                params['width'] = self.width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GoodsInfoIstd()
        if 'delivery_info' in d:
            o.delivery_info = d['delivery_info']
        if 'first_class' in d:
            o.first_class = d['first_class']
        if 'height' in d:
            o.height = d['height']
        if 'length' in d:
            o.length = d['length']
        if 'pickup_info' in d:
            o.pickup_info = d['pickup_info']
        if 'price' in d:
            o.price = d['price']
        if 'second_class' in d:
            o.second_class = d['second_class']
        if 'weight' in d:
            o.weight = d['weight']
        if 'width' in d:
            o.width = d['width']
        return o


