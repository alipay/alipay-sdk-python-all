#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StuffStockOutOrderItem(object):

    def __init__(self):
        self._ext_info = None
        self._item_name = None
        self._item_quantity = None
        self._sku_no = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_quantity(self):
        return self._item_quantity

    @item_quantity.setter
    def item_quantity(self, value):
        self._item_quantity = value
    @property
    def sku_no(self):
        return self._sku_no

    @sku_no.setter
    def sku_no(self, value):
        self._sku_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_quantity:
            if hasattr(self.item_quantity, 'to_alipay_dict'):
                params['item_quantity'] = self.item_quantity.to_alipay_dict()
            else:
                params['item_quantity'] = self.item_quantity
        if self.sku_no:
            if hasattr(self.sku_no, 'to_alipay_dict'):
                params['sku_no'] = self.sku_no.to_alipay_dict()
            else:
                params['sku_no'] = self.sku_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StuffStockOutOrderItem()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_quantity' in d:
            o.item_quantity = d['item_quantity']
        if 'sku_no' in d:
            o.sku_no = d['sku_no']
        return o


