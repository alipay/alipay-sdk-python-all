#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleAuctionBidInfoVO(object):

    def __init__(self):
        self._buyer_identify = None
        self._buyer_name = None
        self._buyer_price = None

    @property
    def buyer_identify(self):
        return self._buyer_identify

    @buyer_identify.setter
    def buyer_identify(self, value):
        self._buyer_identify = value
    @property
    def buyer_name(self):
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, value):
        self._buyer_name = value
    @property
    def buyer_price(self):
        return self._buyer_price

    @buyer_price.setter
    def buyer_price(self, value):
        self._buyer_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_identify:
            if hasattr(self.buyer_identify, 'to_alipay_dict'):
                params['buyer_identify'] = self.buyer_identify.to_alipay_dict()
            else:
                params['buyer_identify'] = self.buyer_identify
        if self.buyer_name:
            if hasattr(self.buyer_name, 'to_alipay_dict'):
                params['buyer_name'] = self.buyer_name.to_alipay_dict()
            else:
                params['buyer_name'] = self.buyer_name
        if self.buyer_price:
            if hasattr(self.buyer_price, 'to_alipay_dict'):
                params['buyer_price'] = self.buyer_price.to_alipay_dict()
            else:
                params['buyer_price'] = self.buyer_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleAuctionBidInfoVO()
        if 'buyer_identify' in d:
            o.buyer_identify = d['buyer_identify']
        if 'buyer_name' in d:
            o.buyer_name = d['buyer_name']
        if 'buyer_price' in d:
            o.buyer_price = d['buyer_price']
        return o


