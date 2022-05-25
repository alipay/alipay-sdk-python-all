#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GoodsInventoryDetail(object):

    def __init__(self):
        self._id = None
        self._inventory = None
        self._sku_id = None
        self._type = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GoodsInventoryDetail()
        if 'id' in d:
            o.id = d['id']
        if 'inventory' in d:
            o.inventory = d['inventory']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'type' in d:
            o.type = d['type']
        return o


