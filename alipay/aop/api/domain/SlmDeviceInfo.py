#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SlmDeviceInfo(object):

    def __init__(self):
        self._brand = None
        self._platform = None
        self._product = None
        self._scope = None
        self._sn = None
        self._support = None

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = value
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
    @property
    def scope(self):
        return self._scope

    @scope.setter
    def scope(self, value):
        self._scope = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def support(self):
        return self._support

    @support.setter
    def support(self, value):
        self._support = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand:
            if hasattr(self.brand, 'to_alipay_dict'):
                params['brand'] = self.brand.to_alipay_dict()
            else:
                params['brand'] = self.brand
        if self.platform:
            if hasattr(self.platform, 'to_alipay_dict'):
                params['platform'] = self.platform.to_alipay_dict()
            else:
                params['platform'] = self.platform
        if self.product:
            if hasattr(self.product, 'to_alipay_dict'):
                params['product'] = self.product.to_alipay_dict()
            else:
                params['product'] = self.product
        if self.scope:
            if hasattr(self.scope, 'to_alipay_dict'):
                params['scope'] = self.scope.to_alipay_dict()
            else:
                params['scope'] = self.scope
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.support:
            if hasattr(self.support, 'to_alipay_dict'):
                params['support'] = self.support.to_alipay_dict()
            else:
                params['support'] = self.support
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SlmDeviceInfo()
        if 'brand' in d:
            o.brand = d['brand']
        if 'platform' in d:
            o.platform = d['platform']
        if 'product' in d:
            o.product = d['product']
        if 'scope' in d:
            o.scope = d['scope']
        if 'sn' in d:
            o.sn = d['sn']
        if 'support' in d:
            o.support = d['support']
        return o


