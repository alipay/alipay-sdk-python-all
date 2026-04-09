#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LtOrderDTO import LtOrderDTO


class LtBidAskLevelDTO(object):

    def __init__(self):
        self._big_order_percent = None
        self._orders = None
        self._price = None
        self._seat_count = None
        self._volume = None

    @property
    def big_order_percent(self):
        return self._big_order_percent

    @big_order_percent.setter
    def big_order_percent(self, value):
        self._big_order_percent = value
    @property
    def orders(self):
        return self._orders

    @orders.setter
    def orders(self, value):
        if isinstance(value, list):
            self._orders = list()
            for i in value:
                if isinstance(i, LtOrderDTO):
                    self._orders.append(i)
                else:
                    self._orders.append(LtOrderDTO.from_alipay_dict(i))
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def seat_count(self):
        return self._seat_count

    @seat_count.setter
    def seat_count(self, value):
        self._seat_count = value
    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value


    def to_alipay_dict(self):
        params = dict()
        if self.big_order_percent:
            if hasattr(self.big_order_percent, 'to_alipay_dict'):
                params['big_order_percent'] = self.big_order_percent.to_alipay_dict()
            else:
                params['big_order_percent'] = self.big_order_percent
        if self.orders:
            if isinstance(self.orders, list):
                for i in range(0, len(self.orders)):
                    element = self.orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.orders[i] = element.to_alipay_dict()
            if hasattr(self.orders, 'to_alipay_dict'):
                params['orders'] = self.orders.to_alipay_dict()
            else:
                params['orders'] = self.orders
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.seat_count:
            if hasattr(self.seat_count, 'to_alipay_dict'):
                params['seat_count'] = self.seat_count.to_alipay_dict()
            else:
                params['seat_count'] = self.seat_count
        if self.volume:
            if hasattr(self.volume, 'to_alipay_dict'):
                params['volume'] = self.volume.to_alipay_dict()
            else:
                params['volume'] = self.volume
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LtBidAskLevelDTO()
        if 'big_order_percent' in d:
            o.big_order_percent = d['big_order_percent']
        if 'orders' in d:
            o.orders = d['orders']
        if 'price' in d:
            o.price = d['price']
        if 'seat_count' in d:
            o.seat_count = d['seat_count']
        if 'volume' in d:
            o.volume = d['volume']
        return o


