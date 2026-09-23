#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalItemUpcexistQueryModel(object):

    def __init__(self):
        self._item_status = None
        self._sku_status = None
        self._store_id = None
        self._upc_list = None

    @property
    def item_status(self):
        return self._item_status

    @item_status.setter
    def item_status(self, value):
        self._item_status = value
    @property
    def sku_status(self):
        return self._sku_status

    @sku_status.setter
    def sku_status(self, value):
        self._sku_status = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def upc_list(self):
        return self._upc_list

    @upc_list.setter
    def upc_list(self, value):
        if isinstance(value, list):
            self._upc_list = list()
            for i in value:
                self._upc_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.item_status:
            if hasattr(self.item_status, 'to_alipay_dict'):
                params['item_status'] = self.item_status.to_alipay_dict()
            else:
                params['item_status'] = self.item_status
        if self.sku_status:
            if hasattr(self.sku_status, 'to_alipay_dict'):
                params['sku_status'] = self.sku_status.to_alipay_dict()
            else:
                params['sku_status'] = self.sku_status
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.upc_list:
            if isinstance(self.upc_list, list):
                for i in range(0, len(self.upc_list)):
                    element = self.upc_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.upc_list[i] = element.to_alipay_dict()
            if hasattr(self.upc_list, 'to_alipay_dict'):
                params['upc_list'] = self.upc_list.to_alipay_dict()
            else:
                params['upc_list'] = self.upc_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalItemUpcexistQueryModel()
        if 'item_status' in d:
            o.item_status = d['item_status']
        if 'sku_status' in d:
            o.sku_status = d['sku_status']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'upc_list' in d:
            o.upc_list = d['upc_list']
        return o


