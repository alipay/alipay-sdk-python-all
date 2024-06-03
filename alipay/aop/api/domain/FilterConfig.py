#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FilterDataConfig import FilterDataConfig


class FilterConfig(object):

    def __init__(self):
        self._data = None
        self._icon = None
        self._key = None
        self._price = None
        self._text = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, FilterDataConfig):
            self._data = value
        else:
            self._data = FilterDataConfig.from_alipay_dict(value)
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FilterConfig()
        if 'data' in d:
            o.data = d['data']
        if 'icon' in d:
            o.icon = d['icon']
        if 'key' in d:
            o.key = d['key']
        if 'price' in d:
            o.price = d['price']
        if 'text' in d:
            o.text = d['text']
        return o


