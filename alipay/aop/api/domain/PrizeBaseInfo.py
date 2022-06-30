#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrizeBaseInfo(object):

    def __init__(self):
        self._fix_price = None
        self._gmt_begin = None
        self._gmt_end = None
        self._modulus = None
        self._prize_id = None
        self._prize_name = None
        self._prize_type = None

    @property
    def fix_price(self):
        return self._fix_price

    @fix_price.setter
    def fix_price(self, value):
        self._fix_price = value
    @property
    def gmt_begin(self):
        return self._gmt_begin

    @gmt_begin.setter
    def gmt_begin(self, value):
        self._gmt_begin = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
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
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.fix_price:
            if hasattr(self.fix_price, 'to_alipay_dict'):
                params['fix_price'] = self.fix_price.to_alipay_dict()
            else:
                params['fix_price'] = self.fix_price
        if self.gmt_begin:
            if hasattr(self.gmt_begin, 'to_alipay_dict'):
                params['gmt_begin'] = self.gmt_begin.to_alipay_dict()
            else:
                params['gmt_begin'] = self.gmt_begin
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
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
        o = PrizeBaseInfo()
        if 'fix_price' in d:
            o.fix_price = d['fix_price']
        if 'gmt_begin' in d:
            o.gmt_begin = d['gmt_begin']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'modulus' in d:
            o.modulus = d['modulus']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        return o


