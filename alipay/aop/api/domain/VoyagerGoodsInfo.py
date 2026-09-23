#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyDTO import MultiCurrencyMoneyDTO


class VoyagerGoodsInfo(object):

    def __init__(self):
        self._biz_amount = None
        self._extend_params = None
        self._goods_id = None

    @property
    def biz_amount(self):
        return self._biz_amount

    @biz_amount.setter
    def biz_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyDTO):
            self._biz_amount = value
        else:
            self._biz_amount = MultiCurrencyMoneyDTO.from_alipay_dict(value)
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_amount:
            if hasattr(self.biz_amount, 'to_alipay_dict'):
                params['biz_amount'] = self.biz_amount.to_alipay_dict()
            else:
                params['biz_amount'] = self.biz_amount
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
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
        o = VoyagerGoodsInfo()
        if 'biz_amount' in d:
            o.biz_amount = d['biz_amount']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        return o


