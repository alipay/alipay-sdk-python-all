#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopThirdPartyInfo(object):

    def __init__(self):
        self._store_id = None
        self._store_logo_url = None
        self._store_name = None

    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_logo_url(self):
        return self._store_logo_url

    @store_logo_url.setter
    def store_logo_url(self, value):
        self._store_logo_url = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.store_logo_url:
            if hasattr(self.store_logo_url, 'to_alipay_dict'):
                params['store_logo_url'] = self.store_logo_url.to_alipay_dict()
            else:
                params['store_logo_url'] = self.store_logo_url
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
        o = ShopThirdPartyInfo()
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_logo_url' in d:
            o.store_logo_url = d['store_logo_url']
        if 'store_name' in d:
            o.store_name = d['store_name']
        return o


