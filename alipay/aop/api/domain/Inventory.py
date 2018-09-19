#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Inventory(object):

    def __init__(self):
        self._batch_code = None
        self._expire_date = None
        self._extend_props = None
        self._gmt_create = None
        self._gmt_modified = None
        self._goods_code = None
        self._inventory_type = None
        self._lock_quantity = None
        self._product_date = None
        self._quantity = None
        self._real_quantity = None
        self._warehouse_code = None

    @property
    def batch_code(self):
        return self._batch_code

    @batch_code.setter
    def batch_code(self, value):
        self._batch_code = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def extend_props(self):
        return self._extend_props

    @extend_props.setter
    def extend_props(self, value):
        self._extend_props = value
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
    def inventory_type(self):
        return self._inventory_type

    @inventory_type.setter
    def inventory_type(self, value):
        self._inventory_type = value
    @property
    def lock_quantity(self):
        return self._lock_quantity

    @lock_quantity.setter
    def lock_quantity(self, value):
        self._lock_quantity = value
    @property
    def product_date(self):
        return self._product_date

    @product_date.setter
    def product_date(self, value):
        self._product_date = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def real_quantity(self):
        return self._real_quantity

    @real_quantity.setter
    def real_quantity(self, value):
        self._real_quantity = value
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_code:
            if hasattr(self.batch_code, 'to_alipay_dict'):
                params['batch_code'] = self.batch_code.to_alipay_dict()
            else:
                params['batch_code'] = self.batch_code
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.extend_props:
            if hasattr(self.extend_props, 'to_alipay_dict'):
                params['extend_props'] = self.extend_props.to_alipay_dict()
            else:
                params['extend_props'] = self.extend_props
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
        if self.inventory_type:
            if hasattr(self.inventory_type, 'to_alipay_dict'):
                params['inventory_type'] = self.inventory_type.to_alipay_dict()
            else:
                params['inventory_type'] = self.inventory_type
        if self.lock_quantity:
            if hasattr(self.lock_quantity, 'to_alipay_dict'):
                params['lock_quantity'] = self.lock_quantity.to_alipay_dict()
            else:
                params['lock_quantity'] = self.lock_quantity
        if self.product_date:
            if hasattr(self.product_date, 'to_alipay_dict'):
                params['product_date'] = self.product_date.to_alipay_dict()
            else:
                params['product_date'] = self.product_date
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.real_quantity:
            if hasattr(self.real_quantity, 'to_alipay_dict'):
                params['real_quantity'] = self.real_quantity.to_alipay_dict()
            else:
                params['real_quantity'] = self.real_quantity
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
        o = Inventory()
        if 'batch_code' in d:
            o.batch_code = d['batch_code']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'extend_props' in d:
            o.extend_props = d['extend_props']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'goods_code' in d:
            o.goods_code = d['goods_code']
        if 'inventory_type' in d:
            o.inventory_type = d['inventory_type']
        if 'lock_quantity' in d:
            o.lock_quantity = d['lock_quantity']
        if 'product_date' in d:
            o.product_date = d['product_date']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'real_quantity' in d:
            o.real_quantity = d['real_quantity']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        return o


