#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyDTO import MultiCurrencyMoneyDTO
from alipay.aop.api.domain.MultiCurrencyMoneyDTO import MultiCurrencyMoneyDTO


class OrderPriceParam(object):

    def __init__(self):
        self._order_amount = None
        self._supplier_discount = None

    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyDTO):
            self._order_amount = value
        else:
            self._order_amount = MultiCurrencyMoneyDTO.from_alipay_dict(value)
    @property
    def supplier_discount(self):
        return self._supplier_discount

    @supplier_discount.setter
    def supplier_discount(self, value):
        if isinstance(value, MultiCurrencyMoneyDTO):
            self._supplier_discount = value
        else:
            self._supplier_discount = MultiCurrencyMoneyDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.supplier_discount:
            if hasattr(self.supplier_discount, 'to_alipay_dict'):
                params['supplier_discount'] = self.supplier_discount.to_alipay_dict()
            else:
                params['supplier_discount'] = self.supplier_discount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderPriceParam()
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'supplier_discount' in d:
            o.supplier_discount = d['supplier_discount']
        return o


