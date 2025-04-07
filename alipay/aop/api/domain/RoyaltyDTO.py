#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RoyaltyDTO(object):

    def __init__(self):
        self._buy_out_price = None
        self._expect_royalty_time = None
        self._royalty_period = None
        self._royalty_price = None
        self._royalty_type = None

    @property
    def buy_out_price(self):
        return self._buy_out_price

    @buy_out_price.setter
    def buy_out_price(self, value):
        self._buy_out_price = value
    @property
    def expect_royalty_time(self):
        return self._expect_royalty_time

    @expect_royalty_time.setter
    def expect_royalty_time(self, value):
        self._expect_royalty_time = value
    @property
    def royalty_period(self):
        return self._royalty_period

    @royalty_period.setter
    def royalty_period(self, value):
        self._royalty_period = value
    @property
    def royalty_price(self):
        return self._royalty_price

    @royalty_price.setter
    def royalty_price(self, value):
        self._royalty_price = value
    @property
    def royalty_type(self):
        return self._royalty_type

    @royalty_type.setter
    def royalty_type(self, value):
        self._royalty_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.buy_out_price:
            if hasattr(self.buy_out_price, 'to_alipay_dict'):
                params['buy_out_price'] = self.buy_out_price.to_alipay_dict()
            else:
                params['buy_out_price'] = self.buy_out_price
        if self.expect_royalty_time:
            if hasattr(self.expect_royalty_time, 'to_alipay_dict'):
                params['expect_royalty_time'] = self.expect_royalty_time.to_alipay_dict()
            else:
                params['expect_royalty_time'] = self.expect_royalty_time
        if self.royalty_period:
            if hasattr(self.royalty_period, 'to_alipay_dict'):
                params['royalty_period'] = self.royalty_period.to_alipay_dict()
            else:
                params['royalty_period'] = self.royalty_period
        if self.royalty_price:
            if hasattr(self.royalty_price, 'to_alipay_dict'):
                params['royalty_price'] = self.royalty_price.to_alipay_dict()
            else:
                params['royalty_price'] = self.royalty_price
        if self.royalty_type:
            if hasattr(self.royalty_type, 'to_alipay_dict'):
                params['royalty_type'] = self.royalty_type.to_alipay_dict()
            else:
                params['royalty_type'] = self.royalty_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoyaltyDTO()
        if 'buy_out_price' in d:
            o.buy_out_price = d['buy_out_price']
        if 'expect_royalty_time' in d:
            o.expect_royalty_time = d['expect_royalty_time']
        if 'royalty_period' in d:
            o.royalty_period = d['royalty_period']
        if 'royalty_price' in d:
            o.royalty_price = d['royalty_price']
        if 'royalty_type' in d:
            o.royalty_type = d['royalty_type']
        return o


