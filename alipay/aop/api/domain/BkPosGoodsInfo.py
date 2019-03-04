#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BkPosGoodsInfo(object):

    def __init__(self):
        self._goods_name = None
        self._goods_price = None

    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def goods_price(self):
        return self._goods_price

    @goods_price.setter
    def goods_price(self, value):
        self._goods_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.goods_price:
            if hasattr(self.goods_price, 'to_alipay_dict'):
                params['goods_price'] = self.goods_price.to_alipay_dict()
            else:
                params['goods_price'] = self.goods_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BkPosGoodsInfo()
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'goods_price' in d:
            o.goods_price = d['goods_price']
        return o


