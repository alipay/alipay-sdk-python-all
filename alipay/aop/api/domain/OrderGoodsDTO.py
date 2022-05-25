#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderGoodsDTO(object):

    def __init__(self):
        self._goods_amount = None
        self._goods_effective_duration = None
        self._goods_id = None
        self._goods_name = None
        self._goods_prd_time = None
        self._item_id = None

    @property
    def goods_amount(self):
        return self._goods_amount

    @goods_amount.setter
    def goods_amount(self, value):
        self._goods_amount = value
    @property
    def goods_effective_duration(self):
        return self._goods_effective_duration

    @goods_effective_duration.setter
    def goods_effective_duration(self, value):
        self._goods_effective_duration = value
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
    def goods_prd_time(self):
        return self._goods_prd_time

    @goods_prd_time.setter
    def goods_prd_time(self, value):
        self._goods_prd_time = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_amount:
            if hasattr(self.goods_amount, 'to_alipay_dict'):
                params['goods_amount'] = self.goods_amount.to_alipay_dict()
            else:
                params['goods_amount'] = self.goods_amount
        if self.goods_effective_duration:
            if hasattr(self.goods_effective_duration, 'to_alipay_dict'):
                params['goods_effective_duration'] = self.goods_effective_duration.to_alipay_dict()
            else:
                params['goods_effective_duration'] = self.goods_effective_duration
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
        if self.goods_prd_time:
            if hasattr(self.goods_prd_time, 'to_alipay_dict'):
                params['goods_prd_time'] = self.goods_prd_time.to_alipay_dict()
            else:
                params['goods_prd_time'] = self.goods_prd_time
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderGoodsDTO()
        if 'goods_amount' in d:
            o.goods_amount = d['goods_amount']
        if 'goods_effective_duration' in d:
            o.goods_effective_duration = d['goods_effective_duration']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'goods_prd_time' in d:
            o.goods_prd_time = d['goods_prd_time']
        if 'item_id' in d:
            o.item_id = d['item_id']
        return o


