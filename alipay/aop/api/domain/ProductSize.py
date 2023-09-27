#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProductSize(object):

    def __init__(self):
        self._product_deep = None
        self._product_height = None
        self._product_width = None

    @property
    def product_deep(self):
        return self._product_deep

    @product_deep.setter
    def product_deep(self, value):
        self._product_deep = value
    @property
    def product_height(self):
        return self._product_height

    @product_height.setter
    def product_height(self, value):
        self._product_height = value
    @property
    def product_width(self):
        return self._product_width

    @product_width.setter
    def product_width(self, value):
        self._product_width = value


    def to_alipay_dict(self):
        params = dict()
        if self.product_deep:
            if hasattr(self.product_deep, 'to_alipay_dict'):
                params['product_deep'] = self.product_deep.to_alipay_dict()
            else:
                params['product_deep'] = self.product_deep
        if self.product_height:
            if hasattr(self.product_height, 'to_alipay_dict'):
                params['product_height'] = self.product_height.to_alipay_dict()
            else:
                params['product_height'] = self.product_height
        if self.product_width:
            if hasattr(self.product_width, 'to_alipay_dict'):
                params['product_width'] = self.product_width.to_alipay_dict()
            else:
                params['product_width'] = self.product_width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductSize()
        if 'product_deep' in d:
            o.product_deep = d['product_deep']
        if 'product_height' in d:
            o.product_height = d['product_height']
        if 'product_width' in d:
            o.product_width = d['product_width']
        return o


