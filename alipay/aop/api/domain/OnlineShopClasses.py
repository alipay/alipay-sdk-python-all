#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OnlineShopClasses(object):

    def __init__(self):
        self._platform_name = None
        self._store_name = None

    @property
    def platform_name(self):
        return self._platform_name

    @platform_name.setter
    def platform_name(self, value):
        self._platform_name = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.platform_name:
            if hasattr(self.platform_name, 'to_alipay_dict'):
                params['platform_name'] = self.platform_name.to_alipay_dict()
            else:
                params['platform_name'] = self.platform_name
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OnlineShopClasses()
        if 'platform_name' in d:
            o.platform_name = d['platform_name']
        if 'store_name' in d:
            o.store_name = d['store_name']
        return o


