#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndustryInvoiceTradeInfo(object):

    def __init__(self):
        self._channel_type = None
        self._trade_no = None
        self._trade_product = None

    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_product(self):
        return self._trade_product

    @trade_product.setter
    def trade_product(self, value):
        self._trade_product = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_product:
            if hasattr(self.trade_product, 'to_alipay_dict'):
                params['trade_product'] = self.trade_product.to_alipay_dict()
            else:
                params['trade_product'] = self.trade_product
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryInvoiceTradeInfo()
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_product' in d:
            o.trade_product = d['trade_product']
        return o


