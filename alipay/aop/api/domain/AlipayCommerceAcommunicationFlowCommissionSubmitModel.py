#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationFlowCommissionSubmitModel(object):

    def __init__(self):
        self._commission_price = None
        self._commission_ratio = None
        self._item_code = None
        self._settlement_ratio = None

    @property
    def commission_price(self):
        return self._commission_price

    @commission_price.setter
    def commission_price(self, value):
        self._commission_price = value
    @property
    def commission_ratio(self):
        return self._commission_ratio

    @commission_ratio.setter
    def commission_ratio(self, value):
        self._commission_ratio = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def settlement_ratio(self):
        return self._settlement_ratio

    @settlement_ratio.setter
    def settlement_ratio(self, value):
        self._settlement_ratio = value


    def to_alipay_dict(self):
        params = dict()
        if self.commission_price:
            if hasattr(self.commission_price, 'to_alipay_dict'):
                params['commission_price'] = self.commission_price.to_alipay_dict()
            else:
                params['commission_price'] = self.commission_price
        if self.commission_ratio:
            if hasattr(self.commission_ratio, 'to_alipay_dict'):
                params['commission_ratio'] = self.commission_ratio.to_alipay_dict()
            else:
                params['commission_ratio'] = self.commission_ratio
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.settlement_ratio:
            if hasattr(self.settlement_ratio, 'to_alipay_dict'):
                params['settlement_ratio'] = self.settlement_ratio.to_alipay_dict()
            else:
                params['settlement_ratio'] = self.settlement_ratio
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationFlowCommissionSubmitModel()
        if 'commission_price' in d:
            o.commission_price = d['commission_price']
        if 'commission_ratio' in d:
            o.commission_ratio = d['commission_ratio']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'settlement_ratio' in d:
            o.settlement_ratio = d['settlement_ratio']
        return o


