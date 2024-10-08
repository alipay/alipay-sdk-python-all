#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentVO(object):

    def __init__(self):
        self._amount_item = None
        self._amount_original = None
        self._amount_user = None
        self._delivery_discount_fee = None
        self._delivery_fee = None
        self._delivery_price = None
        self._distance_markup_price = None
        self._merchant_receive = None
        self._mi_amount = None
        self._packing_fee = None
        self._time_markup_price = None

    @property
    def amount_item(self):
        return self._amount_item

    @amount_item.setter
    def amount_item(self, value):
        self._amount_item = value
    @property
    def amount_original(self):
        return self._amount_original

    @amount_original.setter
    def amount_original(self, value):
        self._amount_original = value
    @property
    def amount_user(self):
        return self._amount_user

    @amount_user.setter
    def amount_user(self, value):
        self._amount_user = value
    @property
    def delivery_discount_fee(self):
        return self._delivery_discount_fee

    @delivery_discount_fee.setter
    def delivery_discount_fee(self, value):
        self._delivery_discount_fee = value
    @property
    def delivery_fee(self):
        return self._delivery_fee

    @delivery_fee.setter
    def delivery_fee(self, value):
        self._delivery_fee = value
    @property
    def delivery_price(self):
        return self._delivery_price

    @delivery_price.setter
    def delivery_price(self, value):
        self._delivery_price = value
    @property
    def distance_markup_price(self):
        return self._distance_markup_price

    @distance_markup_price.setter
    def distance_markup_price(self, value):
        self._distance_markup_price = value
    @property
    def merchant_receive(self):
        return self._merchant_receive

    @merchant_receive.setter
    def merchant_receive(self, value):
        self._merchant_receive = value
    @property
    def mi_amount(self):
        return self._mi_amount

    @mi_amount.setter
    def mi_amount(self, value):
        self._mi_amount = value
    @property
    def packing_fee(self):
        return self._packing_fee

    @packing_fee.setter
    def packing_fee(self, value):
        self._packing_fee = value
    @property
    def time_markup_price(self):
        return self._time_markup_price

    @time_markup_price.setter
    def time_markup_price(self, value):
        self._time_markup_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_item:
            if hasattr(self.amount_item, 'to_alipay_dict'):
                params['amount_item'] = self.amount_item.to_alipay_dict()
            else:
                params['amount_item'] = self.amount_item
        if self.amount_original:
            if hasattr(self.amount_original, 'to_alipay_dict'):
                params['amount_original'] = self.amount_original.to_alipay_dict()
            else:
                params['amount_original'] = self.amount_original
        if self.amount_user:
            if hasattr(self.amount_user, 'to_alipay_dict'):
                params['amount_user'] = self.amount_user.to_alipay_dict()
            else:
                params['amount_user'] = self.amount_user
        if self.delivery_discount_fee:
            if hasattr(self.delivery_discount_fee, 'to_alipay_dict'):
                params['delivery_discount_fee'] = self.delivery_discount_fee.to_alipay_dict()
            else:
                params['delivery_discount_fee'] = self.delivery_discount_fee
        if self.delivery_fee:
            if hasattr(self.delivery_fee, 'to_alipay_dict'):
                params['delivery_fee'] = self.delivery_fee.to_alipay_dict()
            else:
                params['delivery_fee'] = self.delivery_fee
        if self.delivery_price:
            if hasattr(self.delivery_price, 'to_alipay_dict'):
                params['delivery_price'] = self.delivery_price.to_alipay_dict()
            else:
                params['delivery_price'] = self.delivery_price
        if self.distance_markup_price:
            if hasattr(self.distance_markup_price, 'to_alipay_dict'):
                params['distance_markup_price'] = self.distance_markup_price.to_alipay_dict()
            else:
                params['distance_markup_price'] = self.distance_markup_price
        if self.merchant_receive:
            if hasattr(self.merchant_receive, 'to_alipay_dict'):
                params['merchant_receive'] = self.merchant_receive.to_alipay_dict()
            else:
                params['merchant_receive'] = self.merchant_receive
        if self.mi_amount:
            if hasattr(self.mi_amount, 'to_alipay_dict'):
                params['mi_amount'] = self.mi_amount.to_alipay_dict()
            else:
                params['mi_amount'] = self.mi_amount
        if self.packing_fee:
            if hasattr(self.packing_fee, 'to_alipay_dict'):
                params['packing_fee'] = self.packing_fee.to_alipay_dict()
            else:
                params['packing_fee'] = self.packing_fee
        if self.time_markup_price:
            if hasattr(self.time_markup_price, 'to_alipay_dict'):
                params['time_markup_price'] = self.time_markup_price.to_alipay_dict()
            else:
                params['time_markup_price'] = self.time_markup_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentVO()
        if 'amount_item' in d:
            o.amount_item = d['amount_item']
        if 'amount_original' in d:
            o.amount_original = d['amount_original']
        if 'amount_user' in d:
            o.amount_user = d['amount_user']
        if 'delivery_discount_fee' in d:
            o.delivery_discount_fee = d['delivery_discount_fee']
        if 'delivery_fee' in d:
            o.delivery_fee = d['delivery_fee']
        if 'delivery_price' in d:
            o.delivery_price = d['delivery_price']
        if 'distance_markup_price' in d:
            o.distance_markup_price = d['distance_markup_price']
        if 'merchant_receive' in d:
            o.merchant_receive = d['merchant_receive']
        if 'mi_amount' in d:
            o.mi_amount = d['mi_amount']
        if 'packing_fee' in d:
            o.packing_fee = d['packing_fee']
        if 'time_markup_price' in d:
            o.time_markup_price = d['time_markup_price']
        return o


