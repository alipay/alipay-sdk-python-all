#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTravelFliggyAuthorityQueryModel(object):

    def __init__(self):
        self._global_shop_id = None
        self._operator_id = None
        self._operator_type = None
        self._owner_id = None
        self._store_id = None

    @property
    def global_shop_id(self):
        return self._global_shop_id

    @global_shop_id.setter
    def global_shop_id(self, value):
        self._global_shop_id = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.global_shop_id:
            if hasattr(self.global_shop_id, 'to_alipay_dict'):
                params['global_shop_id'] = self.global_shop_id.to_alipay_dict()
            else:
                params['global_shop_id'] = self.global_shop_id
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelFliggyAuthorityQueryModel()
        if 'global_shop_id' in d:
            o.global_shop_id = d['global_shop_id']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


