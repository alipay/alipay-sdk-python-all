#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentOrderPriceInfoDTO(object):

    def __init__(self):
        self._additional_price = None
        self._buyout_price = None
        self._deposit_price = None
        self._freight = None
        self._order_price = None

    @property
    def additional_price(self):
        return self._additional_price

    @additional_price.setter
    def additional_price(self, value):
        self._additional_price = value
    @property
    def buyout_price(self):
        return self._buyout_price

    @buyout_price.setter
    def buyout_price(self, value):
        self._buyout_price = value
    @property
    def deposit_price(self):
        return self._deposit_price

    @deposit_price.setter
    def deposit_price(self, value):
        self._deposit_price = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.additional_price:
            if hasattr(self.additional_price, 'to_alipay_dict'):
                params['additional_price'] = self.additional_price.to_alipay_dict()
            else:
                params['additional_price'] = self.additional_price
        if self.buyout_price:
            if hasattr(self.buyout_price, 'to_alipay_dict'):
                params['buyout_price'] = self.buyout_price.to_alipay_dict()
            else:
                params['buyout_price'] = self.buyout_price
        if self.deposit_price:
            if hasattr(self.deposit_price, 'to_alipay_dict'):
                params['deposit_price'] = self.deposit_price.to_alipay_dict()
            else:
                params['deposit_price'] = self.deposit_price
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentOrderPriceInfoDTO()
        if 'additional_price' in d:
            o.additional_price = d['additional_price']
        if 'buyout_price' in d:
            o.buyout_price = d['buyout_price']
        if 'deposit_price' in d:
            o.deposit_price = d['deposit_price']
        if 'freight' in d:
            o.freight = d['freight']
        if 'order_price' in d:
            o.order_price = d['order_price']
        return o


