#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantCardRechargeOption(object):

    def __init__(self):
        self._recharge_origin_price = None
        self._recharge_sale_price = None

    @property
    def recharge_origin_price(self):
        return self._recharge_origin_price

    @recharge_origin_price.setter
    def recharge_origin_price(self, value):
        self._recharge_origin_price = value
    @property
    def recharge_sale_price(self):
        return self._recharge_sale_price

    @recharge_sale_price.setter
    def recharge_sale_price(self, value):
        self._recharge_sale_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.recharge_origin_price:
            if hasattr(self.recharge_origin_price, 'to_alipay_dict'):
                params['recharge_origin_price'] = self.recharge_origin_price.to_alipay_dict()
            else:
                params['recharge_origin_price'] = self.recharge_origin_price
        if self.recharge_sale_price:
            if hasattr(self.recharge_sale_price, 'to_alipay_dict'):
                params['recharge_sale_price'] = self.recharge_sale_price.to_alipay_dict()
            else:
                params['recharge_sale_price'] = self.recharge_sale_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantCardRechargeOption()
        if 'recharge_origin_price' in d:
            o.recharge_origin_price = d['recharge_origin_price']
        if 'recharge_sale_price' in d:
            o.recharge_sale_price = d['recharge_sale_price']
        return o


