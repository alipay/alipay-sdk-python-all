#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GoodsSafetyInventoryVO(object):

    def __init__(self):
        self._gmt_create = None
        self._gmt_modified = None
        self._goods_code = None
        self._historical_daily_sales = None
        self._min_order_num = None
        self._purchase_cycle = None
        self._safety_inventory = None
        self._target_inventory = None
        self._warehouse_code = None

    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def goods_code(self):
        return self._goods_code

    @goods_code.setter
    def goods_code(self, value):
        self._goods_code = value
    @property
    def historical_daily_sales(self):
        return self._historical_daily_sales

    @historical_daily_sales.setter
    def historical_daily_sales(self, value):
        self._historical_daily_sales = value
    @property
    def min_order_num(self):
        return self._min_order_num

    @min_order_num.setter
    def min_order_num(self, value):
        self._min_order_num = value
    @property
    def purchase_cycle(self):
        return self._purchase_cycle

    @purchase_cycle.setter
    def purchase_cycle(self, value):
        self._purchase_cycle = value
    @property
    def safety_inventory(self):
        return self._safety_inventory

    @safety_inventory.setter
    def safety_inventory(self, value):
        self._safety_inventory = value
    @property
    def target_inventory(self):
        return self._target_inventory

    @target_inventory.setter
    def target_inventory(self, value):
        self._target_inventory = value
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.goods_code:
            if hasattr(self.goods_code, 'to_alipay_dict'):
                params['goods_code'] = self.goods_code.to_alipay_dict()
            else:
                params['goods_code'] = self.goods_code
        if self.historical_daily_sales:
            if hasattr(self.historical_daily_sales, 'to_alipay_dict'):
                params['historical_daily_sales'] = self.historical_daily_sales.to_alipay_dict()
            else:
                params['historical_daily_sales'] = self.historical_daily_sales
        if self.min_order_num:
            if hasattr(self.min_order_num, 'to_alipay_dict'):
                params['min_order_num'] = self.min_order_num.to_alipay_dict()
            else:
                params['min_order_num'] = self.min_order_num
        if self.purchase_cycle:
            if hasattr(self.purchase_cycle, 'to_alipay_dict'):
                params['purchase_cycle'] = self.purchase_cycle.to_alipay_dict()
            else:
                params['purchase_cycle'] = self.purchase_cycle
        if self.safety_inventory:
            if hasattr(self.safety_inventory, 'to_alipay_dict'):
                params['safety_inventory'] = self.safety_inventory.to_alipay_dict()
            else:
                params['safety_inventory'] = self.safety_inventory
        if self.target_inventory:
            if hasattr(self.target_inventory, 'to_alipay_dict'):
                params['target_inventory'] = self.target_inventory.to_alipay_dict()
            else:
                params['target_inventory'] = self.target_inventory
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
        o = GoodsSafetyInventoryVO()
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'goods_code' in d:
            o.goods_code = d['goods_code']
        if 'historical_daily_sales' in d:
            o.historical_daily_sales = d['historical_daily_sales']
        if 'min_order_num' in d:
            o.min_order_num = d['min_order_num']
        if 'purchase_cycle' in d:
            o.purchase_cycle = d['purchase_cycle']
        if 'safety_inventory' in d:
            o.safety_inventory = d['safety_inventory']
        if 'target_inventory' in d:
            o.target_inventory = d['target_inventory']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        return o


