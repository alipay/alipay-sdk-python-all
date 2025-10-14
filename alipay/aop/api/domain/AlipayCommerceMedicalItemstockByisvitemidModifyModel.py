#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemStockUpdateByIsvItemIdParam import ItemStockUpdateByIsvItemIdParam


class AlipayCommerceMedicalItemstockByisvitemidModifyModel(object):

    def __init__(self):
        self._clear_isv_item_id_list = None
        self._isv_store_code = None
        self._item_stock_list = None

    @property
    def clear_isv_item_id_list(self):
        return self._clear_isv_item_id_list

    @clear_isv_item_id_list.setter
    def clear_isv_item_id_list(self, value):
        if isinstance(value, list):
            self._clear_isv_item_id_list = list()
            for i in value:
                self._clear_isv_item_id_list.append(i)
    @property
    def isv_store_code(self):
        return self._isv_store_code

    @isv_store_code.setter
    def isv_store_code(self, value):
        self._isv_store_code = value
    @property
    def item_stock_list(self):
        return self._item_stock_list

    @item_stock_list.setter
    def item_stock_list(self, value):
        if isinstance(value, list):
            self._item_stock_list = list()
            for i in value:
                if isinstance(i, ItemStockUpdateByIsvItemIdParam):
                    self._item_stock_list.append(i)
                else:
                    self._item_stock_list.append(ItemStockUpdateByIsvItemIdParam.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.clear_isv_item_id_list:
            if isinstance(self.clear_isv_item_id_list, list):
                for i in range(0, len(self.clear_isv_item_id_list)):
                    element = self.clear_isv_item_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.clear_isv_item_id_list[i] = element.to_alipay_dict()
            if hasattr(self.clear_isv_item_id_list, 'to_alipay_dict'):
                params['clear_isv_item_id_list'] = self.clear_isv_item_id_list.to_alipay_dict()
            else:
                params['clear_isv_item_id_list'] = self.clear_isv_item_id_list
        if self.isv_store_code:
            if hasattr(self.isv_store_code, 'to_alipay_dict'):
                params['isv_store_code'] = self.isv_store_code.to_alipay_dict()
            else:
                params['isv_store_code'] = self.isv_store_code
        if self.item_stock_list:
            if isinstance(self.item_stock_list, list):
                for i in range(0, len(self.item_stock_list)):
                    element = self.item_stock_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_stock_list[i] = element.to_alipay_dict()
            if hasattr(self.item_stock_list, 'to_alipay_dict'):
                params['item_stock_list'] = self.item_stock_list.to_alipay_dict()
            else:
                params['item_stock_list'] = self.item_stock_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalItemstockByisvitemidModifyModel()
        if 'clear_isv_item_id_list' in d:
            o.clear_isv_item_id_list = d['clear_isv_item_id_list']
        if 'isv_store_code' in d:
            o.isv_store_code = d['isv_store_code']
        if 'item_stock_list' in d:
            o.item_stock_list = d['item_stock_list']
        return o


