#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemInventory(object):

    def __init__(self):
        self._ext_prop = None
        self._external_item_id = None
        self._inventory = None

    @property
    def ext_prop(self):
        return self._ext_prop

    @ext_prop.setter
    def ext_prop(self, value):
        self._ext_prop = value
    @property
    def external_item_id(self):
        return self._external_item_id

    @external_item_id.setter
    def external_item_id(self, value):
        self._external_item_id = value
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_prop:
            if hasattr(self.ext_prop, 'to_alipay_dict'):
                params['ext_prop'] = self.ext_prop.to_alipay_dict()
            else:
                params['ext_prop'] = self.ext_prop
        if self.external_item_id:
            if hasattr(self.external_item_id, 'to_alipay_dict'):
                params['external_item_id'] = self.external_item_id.to_alipay_dict()
            else:
                params['external_item_id'] = self.external_item_id
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemInventory()
        if 'ext_prop' in d:
            o.ext_prop = d['ext_prop']
        if 'external_item_id' in d:
            o.external_item_id = d['external_item_id']
        if 'inventory' in d:
            o.inventory = d['inventory']
        return o


