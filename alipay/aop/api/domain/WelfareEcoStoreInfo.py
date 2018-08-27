#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WelfareEcoStoreInfo(object):

    def __init__(self):
        self._address = None
        self._brand = None
        self._code = None
        self._name = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.brand:
            if hasattr(self.brand, 'to_alipay_dict'):
                params['brand'] = self.brand.to_alipay_dict()
            else:
                params['brand'] = self.brand
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WelfareEcoStoreInfo()
        if 'address' in d:
            o.address = d['address']
        if 'brand' in d:
            o.brand = d['brand']
        if 'code' in d:
            o.code = d['code']
        if 'name' in d:
            o.name = d['name']
        return o


