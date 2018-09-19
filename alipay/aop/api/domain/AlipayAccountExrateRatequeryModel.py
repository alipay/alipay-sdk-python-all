#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAccountExrateRatequeryModel(object):

    def __init__(self):
        self._currency_pair = None

    @property
    def currency_pair(self):
        return self._currency_pair

    @currency_pair.setter
    def currency_pair(self, value):
        self._currency_pair = value


    def to_alipay_dict(self):
        params = dict()
        if self.currency_pair:
            if hasattr(self.currency_pair, 'to_alipay_dict'):
                params['currency_pair'] = self.currency_pair.to_alipay_dict()
            else:
                params['currency_pair'] = self.currency_pair
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountExrateRatequeryModel()
        if 'currency_pair' in d:
            o.currency_pair = d['currency_pair']
        return o


