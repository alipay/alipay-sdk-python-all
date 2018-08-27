#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MaitainShopProduct import MaitainShopProduct


class AlipayEcoMycarMaintainServiceproductUpdateModel(object):

    def __init__(self):
        self._operation_type = None
        self._out_product_id = None
        self._shop_product = None

    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def out_product_id(self):
        return self._out_product_id

    @out_product_id.setter
    def out_product_id(self, value):
        self._out_product_id = value
    @property
    def shop_product(self):
        return self._shop_product

    @shop_product.setter
    def shop_product(self, value):
        if isinstance(value, MaitainShopProduct):
            self._shop_product = value
        else:
            self._shop_product = MaitainShopProduct.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.out_product_id:
            if hasattr(self.out_product_id, 'to_alipay_dict'):
                params['out_product_id'] = self.out_product_id.to_alipay_dict()
            else:
                params['out_product_id'] = self.out_product_id
        if self.shop_product:
            if hasattr(self.shop_product, 'to_alipay_dict'):
                params['shop_product'] = self.shop_product.to_alipay_dict()
            else:
                params['shop_product'] = self.shop_product
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarMaintainServiceproductUpdateModel()
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'out_product_id' in d:
            o.out_product_id = d['out_product_id']
        if 'shop_product' in d:
            o.shop_product = d['shop_product']
        return o


