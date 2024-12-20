#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantPromoDetailInfoVO(object):

    def __init__(self):
        self._sesame_promo_amount = None
        self._voucher_promo_amount = None

    @property
    def sesame_promo_amount(self):
        return self._sesame_promo_amount

    @sesame_promo_amount.setter
    def sesame_promo_amount(self, value):
        self._sesame_promo_amount = value
    @property
    def voucher_promo_amount(self):
        return self._voucher_promo_amount

    @voucher_promo_amount.setter
    def voucher_promo_amount(self, value):
        self._voucher_promo_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.sesame_promo_amount:
            if hasattr(self.sesame_promo_amount, 'to_alipay_dict'):
                params['sesame_promo_amount'] = self.sesame_promo_amount.to_alipay_dict()
            else:
                params['sesame_promo_amount'] = self.sesame_promo_amount
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
        o = MerchantPromoDetailInfoVO()
        if 'sesame_promo_amount' in d:
            o.sesame_promo_amount = d['sesame_promo_amount']
        if 'voucher_promo_amount' in d:
            o.voucher_promo_amount = d['voucher_promo_amount']
        return o


