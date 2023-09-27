#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportPromotionRecommendQueryModel(object):

    def __init__(self):
        self._amount = None
        self._promo_tag = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def promo_tag(self):
        return self._promo_tag

    @promo_tag.setter
    def promo_tag(self, value):
        self._promo_tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.promo_tag:
            if hasattr(self.promo_tag, 'to_alipay_dict'):
                params['promo_tag'] = self.promo_tag.to_alipay_dict()
            else:
                params['promo_tag'] = self.promo_tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportPromotionRecommendQueryModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'promo_tag' in d:
            o.promo_tag = d['promo_tag']
        return o


