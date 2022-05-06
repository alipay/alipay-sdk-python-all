#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GoodsInfoDTO(object):

    def __init__(self):
        self._goods_amount = None
        self._goods_count = None
        self._goods_id = None
        self._goods_name = None

    @property
    def goods_amount(self):
        return self._goods_amount

    @goods_amount.setter
    def goods_amount(self, value):
        self._goods_amount = value
    @property
    def goods_count(self):
        return self._goods_count

    @goods_count.setter
    def goods_count(self, value):
        self._goods_count = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.goods_amount:
            if hasattr(self.goods_amount, 'to_alipay_dict'):
                params['goods_amount'] = self.goods_amount.to_alipay_dict()
            else:
                params['goods_amount'] = self.goods_amount
        if self.goods_count:
            if hasattr(self.goods_count, 'to_alipay_dict'):
                params['goods_count'] = self.goods_count.to_alipay_dict()
            else:
                params['goods_count'] = self.goods_count
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GoodsInfoDTO()
        if 'goods_amount' in d:
            o.goods_amount = d['goods_amount']
        if 'goods_count' in d:
            o.goods_count = d['goods_count']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        return o


