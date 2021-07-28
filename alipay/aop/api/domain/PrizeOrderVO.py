#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrizeOrderVO(object):

    def __init__(self):
        self._modulus = None
        self._prize_id = None
        self._prize_name = None
        self._prize_order_id = None
        self._prize_type = None

    @property
    def modulus(self):
        return self._modulus

    @modulus.setter
    def modulus(self, value):
        self._modulus = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def prize_order_id(self):
        return self._prize_order_id

    @prize_order_id.setter
    def prize_order_id(self, value):
        self._prize_order_id = value
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.modulus:
            if hasattr(self.modulus, 'to_alipay_dict'):
                params['modulus'] = self.modulus.to_alipay_dict()
            else:
                params['modulus'] = self.modulus
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.prize_order_id:
            if hasattr(self.prize_order_id, 'to_alipay_dict'):
                params['prize_order_id'] = self.prize_order_id.to_alipay_dict()
            else:
                params['prize_order_id'] = self.prize_order_id
        if self.prize_type:
            if hasattr(self.prize_type, 'to_alipay_dict'):
                params['prize_type'] = self.prize_type.to_alipay_dict()
            else:
                params['prize_type'] = self.prize_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrizeOrderVO()
        if 'modulus' in d:
            o.modulus = d['modulus']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'prize_order_id' in d:
            o.prize_order_id = d['prize_order_id']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        return o


