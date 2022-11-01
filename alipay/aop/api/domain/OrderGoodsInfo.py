#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderGoodsInfo(object):

    def __init__(self):
        self._goods_desc = None
        self._goods_id = None
        self._goods_name = None
        self._goods_pic = None
        self._goods_specs = None
        self._quantity = None
        self._unit_price = None

    @property
    def goods_desc(self):
        return self._goods_desc

    @goods_desc.setter
    def goods_desc(self, value):
        self._goods_desc = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def goods_pic(self):
        return self._goods_pic

    @goods_pic.setter
    def goods_pic(self, value):
        self._goods_pic = value
    @property
    def goods_specs(self):
        return self._goods_specs

    @goods_specs.setter
    def goods_specs(self, value):
        self._goods_specs = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_desc:
            if hasattr(self.goods_desc, 'to_alipay_dict'):
                params['goods_desc'] = self.goods_desc.to_alipay_dict()
            else:
                params['goods_desc'] = self.goods_desc
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.goods_pic:
            if hasattr(self.goods_pic, 'to_alipay_dict'):
                params['goods_pic'] = self.goods_pic.to_alipay_dict()
            else:
                params['goods_pic'] = self.goods_pic
        if self.goods_specs:
            if hasattr(self.goods_specs, 'to_alipay_dict'):
                params['goods_specs'] = self.goods_specs.to_alipay_dict()
            else:
                params['goods_specs'] = self.goods_specs
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderGoodsInfo()
        if 'goods_desc' in d:
            o.goods_desc = d['goods_desc']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'goods_pic' in d:
            o.goods_pic = d['goods_pic']
        if 'goods_specs' in d:
            o.goods_specs = d['goods_specs']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        return o


