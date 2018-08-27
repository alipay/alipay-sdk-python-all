#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipayOfflineTrade import AlipayOfflineTrade


class AlipayCommerceTransportOfflinepayTradeSettleModel(object):

    def __init__(self):
        self._trade_list = None

    @property
    def trade_list(self):
        return self._trade_list

    @trade_list.setter
    def trade_list(self, value):
        if isinstance(value, list):
            self._trade_list = list()
            for i in value:
                if isinstance(i, AlipayOfflineTrade):
                    self._trade_list.append(i)
                else:
                    self._trade_list.append(AlipayOfflineTrade.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.trade_list:
            if isinstance(self.trade_list, list):
                for i in range(0, len(self.trade_list)):
                    element = self.trade_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trade_list[i] = element.to_alipay_dict()
            if hasattr(self.trade_list, 'to_alipay_dict'):
                params['trade_list'] = self.trade_list.to_alipay_dict()
            else:
                params['trade_list'] = self.trade_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportOfflinepayTradeSettleModel()
        if 'trade_list' in d:
            o.trade_list = d['trade_list']
        return o


