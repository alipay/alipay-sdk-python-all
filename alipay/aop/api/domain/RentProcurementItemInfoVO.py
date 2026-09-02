#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentProcurementItemInfoVO(object):

    def __init__(self):
        self._item_cnt = None
        self._out_item_id = None
        self._out_sku_id = None
        self._supplier_item_id = None
        self._supplier_item_name = None
        self._supplier_sku_id = None

    @property
    def item_cnt(self):
        return self._item_cnt

    @item_cnt.setter
    def item_cnt(self, value):
        self._item_cnt = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def supplier_item_id(self):
        return self._supplier_item_id

    @supplier_item_id.setter
    def supplier_item_id(self, value):
        self._supplier_item_id = value
    @property
    def supplier_item_name(self):
        return self._supplier_item_name

    @supplier_item_name.setter
    def supplier_item_name(self, value):
        self._supplier_item_name = value
    @property
    def supplier_sku_id(self):
        return self._supplier_sku_id

    @supplier_sku_id.setter
    def supplier_sku_id(self, value):
        self._supplier_sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_cnt:
            if hasattr(self.item_cnt, 'to_alipay_dict'):
                params['item_cnt'] = self.item_cnt.to_alipay_dict()
            else:
                params['item_cnt'] = self.item_cnt
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.supplier_item_id:
            if hasattr(self.supplier_item_id, 'to_alipay_dict'):
                params['supplier_item_id'] = self.supplier_item_id.to_alipay_dict()
            else:
                params['supplier_item_id'] = self.supplier_item_id
        if self.supplier_item_name:
            if hasattr(self.supplier_item_name, 'to_alipay_dict'):
                params['supplier_item_name'] = self.supplier_item_name.to_alipay_dict()
            else:
                params['supplier_item_name'] = self.supplier_item_name
        if self.supplier_sku_id:
            if hasattr(self.supplier_sku_id, 'to_alipay_dict'):
                params['supplier_sku_id'] = self.supplier_sku_id.to_alipay_dict()
            else:
                params['supplier_sku_id'] = self.supplier_sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentProcurementItemInfoVO()
        if 'item_cnt' in d:
            o.item_cnt = d['item_cnt']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'supplier_item_id' in d:
            o.supplier_item_id = d['supplier_item_id']
        if 'supplier_item_name' in d:
            o.supplier_item_name = d['supplier_item_name']
        if 'supplier_sku_id' in d:
            o.supplier_sku_id = d['supplier_sku_id']
        return o


