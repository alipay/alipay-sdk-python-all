#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppItemSkuDiffVO(object):

    def __init__(self):
        self._bar_code = None
        self._original_price = None
        self._out_sku_id = None
        self._sale_price = None
        self._sale_status = None
        self._sku_modify_type = None
        self._stock_num = None
        self._thumb_img = None

    @property
    def bar_code(self):
        return self._bar_code

    @bar_code.setter
    def bar_code(self, value):
        self._bar_code = value
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
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def sale_status(self):
        return self._sale_status

    @sale_status.setter
    def sale_status(self, value):
        self._sale_status = value
    @property
    def sku_modify_type(self):
        return self._sku_modify_type

    @sku_modify_type.setter
    def sku_modify_type(self, value):
        self._sku_modify_type = value
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value
    @property
    def thumb_img(self):
        return self._thumb_img

    @thumb_img.setter
    def thumb_img(self, value):
        self._thumb_img = value


    def to_alipay_dict(self):
        params = dict()
        if self.bar_code:
            if hasattr(self.bar_code, 'to_alipay_dict'):
                params['bar_code'] = self.bar_code.to_alipay_dict()
            else:
                params['bar_code'] = self.bar_code
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
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.sale_status:
            if hasattr(self.sale_status, 'to_alipay_dict'):
                params['sale_status'] = self.sale_status.to_alipay_dict()
            else:
                params['sale_status'] = self.sale_status
        if self.sku_modify_type:
            if hasattr(self.sku_modify_type, 'to_alipay_dict'):
                params['sku_modify_type'] = self.sku_modify_type.to_alipay_dict()
            else:
                params['sku_modify_type'] = self.sku_modify_type
        if self.stock_num:
            if hasattr(self.stock_num, 'to_alipay_dict'):
                params['stock_num'] = self.stock_num.to_alipay_dict()
            else:
                params['stock_num'] = self.stock_num
        if self.thumb_img:
            if hasattr(self.thumb_img, 'to_alipay_dict'):
                params['thumb_img'] = self.thumb_img.to_alipay_dict()
            else:
                params['thumb_img'] = self.thumb_img
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppItemSkuDiffVO()
        if 'bar_code' in d:
            o.bar_code = d['bar_code']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'sale_status' in d:
            o.sale_status = d['sale_status']
        if 'sku_modify_type' in d:
            o.sku_modify_type = d['sku_modify_type']
        if 'stock_num' in d:
            o.stock_num = d['stock_num']
        if 'thumb_img' in d:
            o.thumb_img = d['thumb_img']
        return o


