#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleMarketPriceCreateRequest import RecycleMarketPriceCreateRequest


class AlipayCommerceRecycleMarketpriceSyncModel(object):

    def __init__(self):
        self._market_price_list = None

    @property
    def market_price_list(self):
        return self._market_price_list

    @market_price_list.setter
    def market_price_list(self, value):
        if isinstance(value, list):
            self._market_price_list = list()
            for i in value:
                if isinstance(i, RecycleMarketPriceCreateRequest):
                    self._market_price_list.append(i)
                else:
                    self._market_price_list.append(RecycleMarketPriceCreateRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.market_price_list:
            if isinstance(self.market_price_list, list):
                for i in range(0, len(self.market_price_list)):
                    element = self.market_price_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.market_price_list[i] = element.to_alipay_dict()
            if hasattr(self.market_price_list, 'to_alipay_dict'):
                params['market_price_list'] = self.market_price_list.to_alipay_dict()
            else:
                params['market_price_list'] = self.market_price_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRecycleMarketpriceSyncModel()
        if 'market_price_list' in d:
            o.market_price_list = d['market_price_list']
        return o


