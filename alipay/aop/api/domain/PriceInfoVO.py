#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PriceInfoVO(object):

    def __init__(self):
        self._additional_price = None
        self._discounted_price = None
        self._freight = None
        self._order_price = None
        self._receipt_amount = None

    @property
    def additional_price(self):
        return self._additional_price

    @additional_price.setter
    def additional_price(self, value):
        self._additional_price = value
    @property
    def discounted_price(self):
        return self._discounted_price

    @discounted_price.setter
    def discounted_price(self, value):
        self._discounted_price = value
    @property
    def freight(self):
        return self._freight

    @freight.setter
    def freight(self, value):
        self._freight = value
    @property
    def order_price(self):
        return self._order_price

    @order_price.setter
    def order_price(self, value):
        self._order_price = value
    @property
    def receipt_amount(self):
        return self._receipt_amount

    @receipt_amount.setter
    def receipt_amount(self, value):
        self._receipt_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.additional_price:
            if hasattr(self.additional_price, 'to_alipay_dict'):
                params['additional_price'] = self.additional_price.to_alipay_dict()
            else:
                params['additional_price'] = self.additional_price
        if self.discounted_price:
            if hasattr(self.discounted_price, 'to_alipay_dict'):
                params['discounted_price'] = self.discounted_price.to_alipay_dict()
            else:
                params['discounted_price'] = self.discounted_price
        if self.freight:
            if hasattr(self.freight, 'to_alipay_dict'):
                params['freight'] = self.freight.to_alipay_dict()
            else:
                params['freight'] = self.freight
        if self.order_price:
            if hasattr(self.order_price, 'to_alipay_dict'):
                params['order_price'] = self.order_price.to_alipay_dict()
            else:
                params['order_price'] = self.order_price
        if self.receipt_amount:
            if hasattr(self.receipt_amount, 'to_alipay_dict'):
                params['receipt_amount'] = self.receipt_amount.to_alipay_dict()
            else:
                params['receipt_amount'] = self.receipt_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PriceInfoVO()
        if 'additional_price' in d:
            o.additional_price = d['additional_price']
        if 'discounted_price' in d:
            o.discounted_price = d['discounted_price']
        if 'freight' in d:
            o.freight = d['freight']
        if 'order_price' in d:
            o.order_price = d['order_price']
        if 'receipt_amount' in d:
            o.receipt_amount = d['receipt_amount']
        return o


