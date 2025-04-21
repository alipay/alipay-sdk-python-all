#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InventoryBean(object):

    def __init__(self):
        self._inventory = None
        self._inventory_id = None
        self._inventory_remain = None

    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value
    @property
    def inventory_id(self):
        return self._inventory_id

    @inventory_id.setter
    def inventory_id(self, value):
        self._inventory_id = value
    @property
    def inventory_remain(self):
        return self._inventory_remain

    @inventory_remain.setter
    def inventory_remain(self, value):
        self._inventory_remain = value


    def to_alipay_dict(self):
        params = dict()
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        if self.inventory_id:
            if hasattr(self.inventory_id, 'to_alipay_dict'):
                params['inventory_id'] = self.inventory_id.to_alipay_dict()
            else:
                params['inventory_id'] = self.inventory_id
        if self.inventory_remain:
            if hasattr(self.inventory_remain, 'to_alipay_dict'):
                params['inventory_remain'] = self.inventory_remain.to_alipay_dict()
            else:
                params['inventory_remain'] = self.inventory_remain
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InventoryBean()
        if 'inventory' in d:
            o.inventory = d['inventory']
        if 'inventory_id' in d:
            o.inventory_id = d['inventory_id']
        if 'inventory_remain' in d:
            o.inventory_remain = d['inventory_remain']
        return o


