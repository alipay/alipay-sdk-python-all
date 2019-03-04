#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemInventory import ItemInventory


class AlipayBusinessItemInventoryExternalSyncModel(object):

    def __init__(self):
        self._inventories = None
        self._request_id = None

    @property
    def inventories(self):
        return self._inventories

    @inventories.setter
    def inventories(self, value):
        if isinstance(value, list):
            self._inventories = list()
            for i in value:
                if isinstance(i, ItemInventory):
                    self._inventories.append(i)
                else:
                    self._inventories.append(ItemInventory.from_alipay_dict(i))
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.inventories:
            if isinstance(self.inventories, list):
                for i in range(0, len(self.inventories)):
                    element = self.inventories[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inventories[i] = element.to_alipay_dict()
            if hasattr(self.inventories, 'to_alipay_dict'):
                params['inventories'] = self.inventories.to_alipay_dict()
            else:
                params['inventories'] = self.inventories
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessItemInventoryExternalSyncModel()
        if 'inventories' in d:
            o.inventories = d['inventories']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


