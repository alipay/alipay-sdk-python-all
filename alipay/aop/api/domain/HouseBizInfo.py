#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HouseBizInfo(object):

    def __init__(self):
        self._house_age = None
        self._house_price = None
        self._house_size = None
        self._house_type = None
        self._image_string = None
        self._page_url = None

    @property
    def house_age(self):
        return self._house_age

    @house_age.setter
    def house_age(self, value):
        self._house_age = value
    @property
    def house_price(self):
        return self._house_price

    @house_price.setter
    def house_price(self, value):
        self._house_price = value
    @property
    def house_size(self):
        return self._house_size

    @house_size.setter
    def house_size(self, value):
        self._house_size = value
    @property
    def house_type(self):
        return self._house_type

    @house_type.setter
    def house_type(self, value):
        self._house_type = value
    @property
    def image_string(self):
        return self._image_string

    @image_string.setter
    def image_string(self, value):
        self._image_string = value
    @property
    def page_url(self):
        return self._page_url

    @page_url.setter
    def page_url(self, value):
        self._page_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.house_age:
            if hasattr(self.house_age, 'to_alipay_dict'):
                params['house_age'] = self.house_age.to_alipay_dict()
            else:
                params['house_age'] = self.house_age
        if self.house_price:
            if hasattr(self.house_price, 'to_alipay_dict'):
                params['house_price'] = self.house_price.to_alipay_dict()
            else:
                params['house_price'] = self.house_price
        if self.house_size:
            if hasattr(self.house_size, 'to_alipay_dict'):
                params['house_size'] = self.house_size.to_alipay_dict()
            else:
                params['house_size'] = self.house_size
        if self.house_type:
            if hasattr(self.house_type, 'to_alipay_dict'):
                params['house_type'] = self.house_type.to_alipay_dict()
            else:
                params['house_type'] = self.house_type
        if self.image_string:
            if hasattr(self.image_string, 'to_alipay_dict'):
                params['image_string'] = self.image_string.to_alipay_dict()
            else:
                params['image_string'] = self.image_string
        if self.page_url:
            if hasattr(self.page_url, 'to_alipay_dict'):
                params['page_url'] = self.page_url.to_alipay_dict()
            else:
                params['page_url'] = self.page_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HouseBizInfo()
        if 'house_age' in d:
            o.house_age = d['house_age']
        if 'house_price' in d:
            o.house_price = d['house_price']
        if 'house_size' in d:
            o.house_size = d['house_size']
        if 'house_type' in d:
            o.house_type = d['house_type']
        if 'image_string' in d:
            o.image_string = d['image_string']
        if 'page_url' in d:
            o.page_url = d['page_url']
        return o


