#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PlatformPromoDetailInfoVO(object):

    def __init__(self):
        self._discount_promo_amount = None
        self._voucher_promo_amount = None

    @property
    def discount_promo_amount(self):
        return self._discount_promo_amount

    @discount_promo_amount.setter
    def discount_promo_amount(self, value):
        self._discount_promo_amount = value
    @property
    def voucher_promo_amount(self):
        return self._voucher_promo_amount

    @voucher_promo_amount.setter
    def voucher_promo_amount(self, value):
        self._voucher_promo_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_promo_amount:
            if hasattr(self.discount_promo_amount, 'to_alipay_dict'):
                params['discount_promo_amount'] = self.discount_promo_amount.to_alipay_dict()
            else:
                params['discount_promo_amount'] = self.discount_promo_amount
        if self.voucher_promo_amount:
            if hasattr(self.voucher_promo_amount, 'to_alipay_dict'):
                params['voucher_promo_amount'] = self.voucher_promo_amount.to_alipay_dict()
            else:
                params['voucher_promo_amount'] = self.voucher_promo_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PlatformPromoDetailInfoVO()
        if 'discount_promo_amount' in d:
            o.discount_promo_amount = d['discount_promo_amount']
        if 'voucher_promo_amount' in d:
            o.voucher_promo_amount = d['voucher_promo_amount']
        return o


