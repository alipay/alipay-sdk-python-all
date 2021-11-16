#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivitySpecialVoucher(object):

    def __init__(self):
        self._floor_amount = None
        self._goods_name = None
        self._origin_amount = None
        self._special_amount = None

    @property
    def floor_amount(self):
        return self._floor_amount

    @floor_amount.setter
    def floor_amount(self, value):
        self._floor_amount = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def origin_amount(self):
        return self._origin_amount

    @origin_amount.setter
    def origin_amount(self, value):
        self._origin_amount = value
    @property
    def special_amount(self):
        return self._special_amount

    @special_amount.setter
    def special_amount(self, value):
        self._special_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.floor_amount:
            if hasattr(self.floor_amount, 'to_alipay_dict'):
                params['floor_amount'] = self.floor_amount.to_alipay_dict()
            else:
                params['floor_amount'] = self.floor_amount
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.origin_amount:
            if hasattr(self.origin_amount, 'to_alipay_dict'):
                params['origin_amount'] = self.origin_amount.to_alipay_dict()
            else:
                params['origin_amount'] = self.origin_amount
        if self.special_amount:
            if hasattr(self.special_amount, 'to_alipay_dict'):
                params['special_amount'] = self.special_amount.to_alipay_dict()
            else:
                params['special_amount'] = self.special_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivitySpecialVoucher()
        if 'floor_amount' in d:
            o.floor_amount = d['floor_amount']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'origin_amount' in d:
            o.origin_amount = d['origin_amount']
        if 'special_amount' in d:
            o.special_amount = d['special_amount']
        return o


