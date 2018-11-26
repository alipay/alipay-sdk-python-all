#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrizeDetail(object):

    def __init__(self):
        self._gmt_time = None
        self._out_prize_id = None
        self._price = None
        self._prize_id = None

    @property
    def gmt_time(self):
        return self._gmt_time

    @gmt_time.setter
    def gmt_time(self, value):
        self._gmt_time = value
    @property
    def out_prize_id(self):
        return self._out_prize_id

    @out_prize_id.setter
    def out_prize_id(self, value):
        self._out_prize_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_time:
            if hasattr(self.gmt_time, 'to_alipay_dict'):
                params['gmt_time'] = self.gmt_time.to_alipay_dict()
            else:
                params['gmt_time'] = self.gmt_time
        if self.out_prize_id:
            if hasattr(self.out_prize_id, 'to_alipay_dict'):
                params['out_prize_id'] = self.out_prize_id.to_alipay_dict()
            else:
                params['out_prize_id'] = self.out_prize_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrizeDetail()
        if 'gmt_time' in d:
            o.gmt_time = d['gmt_time']
        if 'out_prize_id' in d:
            o.out_prize_id = d['out_prize_id']
        if 'price' in d:
            o.price = d['price']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        return o


