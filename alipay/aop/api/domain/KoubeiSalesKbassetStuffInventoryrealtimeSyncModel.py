#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InventoryItem import InventoryItem


class KoubeiSalesKbassetStuffInventoryrealtimeSyncModel(object):

    def __init__(self):
        self._ext_info = None
        self._inventory_time = None
        self._items = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def inventory_time(self):
        return self._inventory_time

    @inventory_time.setter
    def inventory_time(self, value):
        self._inventory_time = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, InventoryItem):
                    self._items.append(i)
                else:
                    self._items.append(InventoryItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.inventory_time:
            if hasattr(self.inventory_time, 'to_alipay_dict'):
                params['inventory_time'] = self.inventory_time.to_alipay_dict()
            else:
                params['inventory_time'] = self.inventory_time
        if self.items:
            if isinstance(self.items, list):
                for i in range(0, len(self.items)):
                    element = self.items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.items[i] = element.to_alipay_dict()
            if hasattr(self.items, 'to_alipay_dict'):
                params['items'] = self.items.to_alipay_dict()
            else:
                params['items'] = self.items
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiSalesKbassetStuffInventoryrealtimeSyncModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'inventory_time' in d:
            o.inventory_time = d['inventory_time']
        if 'items' in d:
            o.items = d['items']
        return o


