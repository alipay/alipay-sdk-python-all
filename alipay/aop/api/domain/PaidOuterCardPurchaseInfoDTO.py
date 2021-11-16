#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaidOuterCardPurchaseInfoDTO(object):

    def __init__(self):
        self._action_date = None
        self._alipay_trade_no = None
        self._out_trade_no = None
        self._price = None
        self._source = None

    @property
    def action_date(self):
        return self._action_date

    @action_date.setter
    def action_date(self, value):
        self._action_date = value
    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_date:
            if hasattr(self.action_date, 'to_alipay_dict'):
                params['action_date'] = self.action_date.to_alipay_dict()
            else:
                params['action_date'] = self.action_date
        if self.alipay_trade_no:
            if hasattr(self.alipay_trade_no, 'to_alipay_dict'):
                params['alipay_trade_no'] = self.alipay_trade_no.to_alipay_dict()
            else:
                params['alipay_trade_no'] = self.alipay_trade_no
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaidOuterCardPurchaseInfoDTO()
        if 'action_date' in d:
            o.action_date = d['action_date']
        if 'alipay_trade_no' in d:
            o.alipay_trade_no = d['alipay_trade_no']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'price' in d:
            o.price = d['price']
        if 'source' in d:
            o.source = d['source']
        return o


