#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InboundOrderLine(object):

    def __init__(self):
        self._batch_code = None
        self._expire_date = None
        self._goods_code = None
        self._inventory_type = None
        self._plan_quantity = None
        self._price = None
        self._product_date = None
        self._remark = None

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
    def plan_quantity(self):
        return self._plan_quantity

    @plan_quantity.setter
    def plan_quantity(self, value):
        self._plan_quantity = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def product_date(self):
        return self._product_date

    @product_date.setter
    def product_date(self, value):
        self._product_date = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


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
        if self.plan_quantity:
            if hasattr(self.plan_quantity, 'to_alipay_dict'):
                params['plan_quantity'] = self.plan_quantity.to_alipay_dict()
            else:
                params['plan_quantity'] = self.plan_quantity
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.product_date:
            if hasattr(self.product_date, 'to_alipay_dict'):
                params['product_date'] = self.product_date.to_alipay_dict()
            else:
                params['product_date'] = self.product_date
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InboundOrderLine()
        if 'batch_code' in d:
            o.batch_code = d['batch_code']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'goods_code' in d:
            o.goods_code = d['goods_code']
        if 'inventory_type' in d:
            o.inventory_type = d['inventory_type']
        if 'plan_quantity' in d:
            o.plan_quantity = d['plan_quantity']
        if 'price' in d:
            o.price = d['price']
        if 'product_date' in d:
            o.product_date = d['product_date']
        if 'remark' in d:
            o.remark = d['remark']
        return o


