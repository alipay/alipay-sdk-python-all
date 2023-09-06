#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MpcProperty import MpcProperty


class MpcSkuVO(object):

    def __init__(self):
        self._barcode = None
        self._mpc_sku_id = None
        self._original_price = None
        self._out_sku_id = None
        self._properties = None
        self._sale_price = None
        self._sku_pic = None
        self._stock_num = None

    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, value):
        self._barcode = value
    @property
    def mpc_sku_id(self):
        return self._mpc_sku_id

    @mpc_sku_id.setter
    def mpc_sku_id(self, value):
        self._mpc_sku_id = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, value):
        if isinstance(value, list):
            self._properties = list()
            for i in value:
                if isinstance(i, MpcProperty):
                    self._properties.append(i)
                else:
                    self._properties.append(MpcProperty.from_alipay_dict(i))
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def sku_pic(self):
        return self._sku_pic

    @sku_pic.setter
    def sku_pic(self, value):
        self._sku_pic = value
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.barcode:
            if hasattr(self.barcode, 'to_alipay_dict'):
                params['barcode'] = self.barcode.to_alipay_dict()
            else:
                params['barcode'] = self.barcode
        if self.mpc_sku_id:
            if hasattr(self.mpc_sku_id, 'to_alipay_dict'):
                params['mpc_sku_id'] = self.mpc_sku_id.to_alipay_dict()
            else:
                params['mpc_sku_id'] = self.mpc_sku_id
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.properties:
            if isinstance(self.properties, list):
                for i in range(0, len(self.properties)):
                    element = self.properties[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.properties[i] = element.to_alipay_dict()
            if hasattr(self.properties, 'to_alipay_dict'):
                params['properties'] = self.properties.to_alipay_dict()
            else:
                params['properties'] = self.properties
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.sku_pic:
            if hasattr(self.sku_pic, 'to_alipay_dict'):
                params['sku_pic'] = self.sku_pic.to_alipay_dict()
            else:
                params['sku_pic'] = self.sku_pic
        if self.stock_num:
            if hasattr(self.stock_num, 'to_alipay_dict'):
                params['stock_num'] = self.stock_num.to_alipay_dict()
            else:
                params['stock_num'] = self.stock_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MpcSkuVO()
        if 'barcode' in d:
            o.barcode = d['barcode']
        if 'mpc_sku_id' in d:
            o.mpc_sku_id = d['mpc_sku_id']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'properties' in d:
            o.properties = d['properties']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'sku_pic' in d:
            o.sku_pic = d['sku_pic']
        if 'stock_num' in d:
            o.stock_num = d['stock_num']
        return o


