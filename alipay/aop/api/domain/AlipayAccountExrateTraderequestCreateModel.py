#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TradeRequestVO import TradeRequestVO


class AlipayAccountExrateTraderequestCreateModel(object):

    def __init__(self):
        self._trade_request = None

    @property
    def trade_request(self):
        return self._trade_request

    @trade_request.setter
    def trade_request(self, value):
        if isinstance(value, TradeRequestVO):
            self._trade_request = value
        else:
            self._trade_request = TradeRequestVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.trade_request:
            if hasattr(self.trade_request, 'to_alipay_dict'):
                params['trade_request'] = self.trade_request.to_alipay_dict()
            else:
                params['trade_request'] = self.trade_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountExrateTraderequestCreateModel()
        if 'trade_request' in d:
            o.trade_request = d['trade_request']
        return o


