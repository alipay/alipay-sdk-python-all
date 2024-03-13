#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DcmealDishDetail(object):

    def __init__(self):
        self._dish_id = None
        self._dish_name = None
        self._dish_price = None
        self._dish_sale_amount = None

    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def dish_name(self):
        return self._dish_name

    @dish_name.setter
    def dish_name(self, value):
        self._dish_name = value
    @property
    def dish_price(self):
        return self._dish_price

    @dish_price.setter
    def dish_price(self, value):
        self._dish_price = value
    @property
    def dish_sale_amount(self):
        return self._dish_sale_amount

    @dish_sale_amount.setter
    def dish_sale_amount(self, value):
        self._dish_sale_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.dish_name:
            if hasattr(self.dish_name, 'to_alipay_dict'):
                params['dish_name'] = self.dish_name.to_alipay_dict()
            else:
                params['dish_name'] = self.dish_name
        if self.dish_price:
            if hasattr(self.dish_price, 'to_alipay_dict'):
                params['dish_price'] = self.dish_price.to_alipay_dict()
            else:
                params['dish_price'] = self.dish_price
        if self.dish_sale_amount:
            if hasattr(self.dish_sale_amount, 'to_alipay_dict'):
                params['dish_sale_amount'] = self.dish_sale_amount.to_alipay_dict()
            else:
                params['dish_sale_amount'] = self.dish_sale_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DcmealDishDetail()
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'dish_name' in d:
            o.dish_name = d['dish_name']
        if 'dish_price' in d:
            o.dish_price = d['dish_price']
        if 'dish_sale_amount' in d:
            o.dish_sale_amount = d['dish_sale_amount']
        return o


