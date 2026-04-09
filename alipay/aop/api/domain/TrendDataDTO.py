#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TrendItemDTO import TrendItemDTO


class TrendDataDTO(object):

    def __init__(self):
        self._channel_exchange = None
        self._items = None
        self._symbol = None

    @property
    def channel_exchange(self):
        return self._channel_exchange

    @channel_exchange.setter
    def channel_exchange(self, value):
        self._channel_exchange = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, TrendItemDTO):
                    self._items.append(i)
                else:
                    self._items.append(TrendItemDTO.from_alipay_dict(i))
    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_exchange:
            if hasattr(self.channel_exchange, 'to_alipay_dict'):
                params['channel_exchange'] = self.channel_exchange.to_alipay_dict()
            else:
                params['channel_exchange'] = self.channel_exchange
        if self.items:
            if isinstance(self.items, list):
                for i in range(0, len(self.items)):
                    element = self.items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.items[i] = element.to_alipay_dict()
            if hasattr(self.items, 'to_alipay_dict'):
                params['items'] = self.items.to_alipay_dict()
            else:
                params['items'] = self.items
        if self.symbol:
            if hasattr(self.symbol, 'to_alipay_dict'):
                params['symbol'] = self.symbol.to_alipay_dict()
            else:
                params['symbol'] = self.symbol
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrendDataDTO()
        if 'channel_exchange' in d:
            o.channel_exchange = d['channel_exchange']
        if 'items' in d:
            o.items = d['items']
        if 'symbol' in d:
            o.symbol = d['symbol']
        return o


