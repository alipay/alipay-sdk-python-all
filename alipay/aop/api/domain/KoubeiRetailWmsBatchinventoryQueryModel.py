#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiRetailWmsBatchinventoryQueryModel(object):

    def __init__(self):
        self._goods_code_list = None
        self._inventory_type = None
        self._warehouse_code = None

    @property
    def goods_code_list(self):
        return self._goods_code_list

    @goods_code_list.setter
    def goods_code_list(self, value):
        if isinstance(value, list):
            self._goods_code_list = list()
            for i in value:
                self._goods_code_list.append(i)
    @property
    def inventory_type(self):
        return self._inventory_type

    @inventory_type.setter
    def inventory_type(self, value):
        self._inventory_type = value
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_code_list:
            if isinstance(self.goods_code_list, list):
                for i in range(0, len(self.goods_code_list)):
                    element = self.goods_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_code_list[i] = element.to_alipay_dict()
            if hasattr(self.goods_code_list, 'to_alipay_dict'):
                params['goods_code_list'] = self.goods_code_list.to_alipay_dict()
            else:
                params['goods_code_list'] = self.goods_code_list
        if self.inventory_type:
            if hasattr(self.inventory_type, 'to_alipay_dict'):
                params['inventory_type'] = self.inventory_type.to_alipay_dict()
            else:
                params['inventory_type'] = self.inventory_type
        if self.warehouse_code:
            if hasattr(self.warehouse_code, 'to_alipay_dict'):
                params['warehouse_code'] = self.warehouse_code.to_alipay_dict()
            else:
                params['warehouse_code'] = self.warehouse_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsBatchinventoryQueryModel()
        if 'goods_code_list' in d:
            o.goods_code_list = d['goods_code_list']
        if 'inventory_type' in d:
            o.inventory_type = d['inventory_type']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        return o


