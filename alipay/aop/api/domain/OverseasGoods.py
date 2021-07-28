#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OverseasGoods(object):

    def __init__(self):
        self._goods_amount = None
        self._goods_id = None

    @property
    def goods_amount(self):
        return self._goods_amount

    @goods_amount.setter
    def goods_amount(self, value):
        self._goods_amount = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_amount:
            if hasattr(self.goods_amount, 'to_alipay_dict'):
                params['goods_amount'] = self.goods_amount.to_alipay_dict()
            else:
                params['goods_amount'] = self.goods_amount
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OverseasGoods()
        if 'goods_amount' in d:
            o.goods_amount = d['goods_amount']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        return o


