#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CateringServiceInfo(object):

    def __init__(self):
        self._service_sub_type = None
        self._shop_id = None
        self._store_address = None
        self._store_id = None
        self._store_name = None

    @property
    def service_sub_type(self):
        return self._service_sub_type

    @service_sub_type.setter
    def service_sub_type(self, value):
        self._service_sub_type = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def store_address(self):
        return self._store_address

    @store_address.setter
    def store_address(self, value):
        self._store_address = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_sub_type:
            if hasattr(self.service_sub_type, 'to_alipay_dict'):
                params['service_sub_type'] = self.service_sub_type.to_alipay_dict()
            else:
                params['service_sub_type'] = self.service_sub_type
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.store_address:
            if hasattr(self.store_address, 'to_alipay_dict'):
                params['store_address'] = self.store_address.to_alipay_dict()
            else:
                params['store_address'] = self.store_address
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
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
        o = CateringServiceInfo()
        if 'service_sub_type' in d:
            o.service_sub_type = d['service_sub_type']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'store_address' in d:
            o.store_address = d['store_address']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_name' in d:
            o.store_name = d['store_name']
        return o


