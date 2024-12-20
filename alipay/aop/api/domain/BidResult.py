#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LoadInfoNode import LoadInfoNode
from alipay.aop.api.domain.LoadInfoNode import LoadInfoNode
from alipay.aop.api.domain.PriceInfoNode import PriceInfoNode


class BidResult(object):

    def __init__(self):
        self._bid_adjustment = None
        self._bid_load = None
        self._bid_price = None

    @property
    def bid_adjustment(self):
        return self._bid_adjustment

    @bid_adjustment.setter
    def bid_adjustment(self, value):
        if isinstance(value, list):
            self._bid_adjustment = list()
            for i in value:
                if isinstance(i, LoadInfoNode):
                    self._bid_adjustment.append(i)
                else:
                    self._bid_adjustment.append(LoadInfoNode.from_alipay_dict(i))
    @property
    def bid_load(self):
        return self._bid_load

    @bid_load.setter
    def bid_load(self, value):
        if isinstance(value, list):
            self._bid_load = list()
            for i in value:
                if isinstance(i, LoadInfoNode):
                    self._bid_load.append(i)
                else:
                    self._bid_load.append(LoadInfoNode.from_alipay_dict(i))
    @property
    def bid_price(self):
        return self._bid_price

    @bid_price.setter
    def bid_price(self, value):
        if isinstance(value, list):
            self._bid_price = list()
            for i in value:
                if isinstance(i, PriceInfoNode):
                    self._bid_price.append(i)
                else:
                    self._bid_price.append(PriceInfoNode.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.bid_adjustment:
            if isinstance(self.bid_adjustment, list):
                for i in range(0, len(self.bid_adjustment)):
                    element = self.bid_adjustment[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bid_adjustment[i] = element.to_alipay_dict()
            if hasattr(self.bid_adjustment, 'to_alipay_dict'):
                params['bid_adjustment'] = self.bid_adjustment.to_alipay_dict()
            else:
                params['bid_adjustment'] = self.bid_adjustment
        if self.bid_load:
            if isinstance(self.bid_load, list):
                for i in range(0, len(self.bid_load)):
                    element = self.bid_load[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bid_load[i] = element.to_alipay_dict()
            if hasattr(self.bid_load, 'to_alipay_dict'):
                params['bid_load'] = self.bid_load.to_alipay_dict()
            else:
                params['bid_load'] = self.bid_load
        if self.bid_price:
            if isinstance(self.bid_price, list):
                for i in range(0, len(self.bid_price)):
                    element = self.bid_price[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bid_price[i] = element.to_alipay_dict()
            if hasattr(self.bid_price, 'to_alipay_dict'):
                params['bid_price'] = self.bid_price.to_alipay_dict()
            else:
                params['bid_price'] = self.bid_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BidResult()
        if 'bid_adjustment' in d:
            o.bid_adjustment = d['bid_adjustment']
        if 'bid_load' in d:
            o.bid_load = d['bid_load']
        if 'bid_price' in d:
            o.bid_price = d['bid_price']
        return o


