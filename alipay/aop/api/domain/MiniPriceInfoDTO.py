#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniPriceInfoDTO(object):

    def __init__(self):
        self._merchant_discount_amount = None
        self._platform_discount_amount = None

    @property
    def merchant_discount_amount(self):
        return self._merchant_discount_amount

    @merchant_discount_amount.setter
    def merchant_discount_amount(self, value):
        self._merchant_discount_amount = value
    @property
    def platform_discount_amount(self):
        return self._platform_discount_amount

    @platform_discount_amount.setter
    def platform_discount_amount(self, value):
        self._platform_discount_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_discount_amount:
            if hasattr(self.merchant_discount_amount, 'to_alipay_dict'):
                params['merchant_discount_amount'] = self.merchant_discount_amount.to_alipay_dict()
            else:
                params['merchant_discount_amount'] = self.merchant_discount_amount
        if self.platform_discount_amount:
            if hasattr(self.platform_discount_amount, 'to_alipay_dict'):
                params['platform_discount_amount'] = self.platform_discount_amount.to_alipay_dict()
            else:
                params['platform_discount_amount'] = self.platform_discount_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniPriceInfoDTO()
        if 'merchant_discount_amount' in d:
            o.merchant_discount_amount = d['merchant_discount_amount']
        if 'platform_discount_amount' in d:
            o.platform_discount_amount = d['platform_discount_amount']
        return o


