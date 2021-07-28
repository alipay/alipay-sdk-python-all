#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarRentalGoods(object):

    def __init__(self):
        self._goods_id = None
        self._goods_name = None
        self._goods_num = None
        self._goods_pic_url = None
        self._goods_price = None
        self._goods_specs = None

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
    def goods_num(self):
        return self._goods_num

    @goods_num.setter
    def goods_num(self, value):
        self._goods_num = value
    @property
    def goods_pic_url(self):
        return self._goods_pic_url

    @goods_pic_url.setter
    def goods_pic_url(self, value):
        self._goods_pic_url = value
    @property
    def goods_price(self):
        return self._goods_price

    @goods_price.setter
    def goods_price(self, value):
        self._goods_price = value
    @property
    def goods_specs(self):
        return self._goods_specs

    @goods_specs.setter
    def goods_specs(self, value):
        self._goods_specs = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.goods_num:
            if hasattr(self.goods_num, 'to_alipay_dict'):
                params['goods_num'] = self.goods_num.to_alipay_dict()
            else:
                params['goods_num'] = self.goods_num
        if self.goods_pic_url:
            if hasattr(self.goods_pic_url, 'to_alipay_dict'):
                params['goods_pic_url'] = self.goods_pic_url.to_alipay_dict()
            else:
                params['goods_pic_url'] = self.goods_pic_url
        if self.goods_price:
            if hasattr(self.goods_price, 'to_alipay_dict'):
                params['goods_price'] = self.goods_price.to_alipay_dict()
            else:
                params['goods_price'] = self.goods_price
        if self.goods_specs:
            if hasattr(self.goods_specs, 'to_alipay_dict'):
                params['goods_specs'] = self.goods_specs.to_alipay_dict()
            else:
                params['goods_specs'] = self.goods_specs
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarRentalGoods()
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'goods_num' in d:
            o.goods_num = d['goods_num']
        if 'goods_pic_url' in d:
            o.goods_pic_url = d['goods_pic_url']
        if 'goods_price' in d:
            o.goods_price = d['goods_price']
        if 'goods_specs' in d:
            o.goods_specs = d['goods_specs']
        return o


