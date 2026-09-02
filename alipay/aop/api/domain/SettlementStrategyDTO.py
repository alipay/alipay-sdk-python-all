#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SettlementStrategyDTO(object):

    def __init__(self):
        self._settlement_currency = None

    @property
    def settlement_currency(self):
        return self._settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, value):
        self._settlement_currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.settlement_currency:
            if hasattr(self.settlement_currency, 'to_alipay_dict'):
                params['settlement_currency'] = self.settlement_currency.to_alipay_dict()
            else:
                params['settlement_currency'] = self.settlement_currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SettlementStrategyDTO()
        if 'settlement_currency' in d:
            o.settlement_currency = d['settlement_currency']
        return o


