#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DiscountInfoData(object):

    def __init__(self):
        self._discount_amount = None
        self._discount_name = None
        self._discount_page_link = None
        self._discount_quantity = None
        self._external_discount_id = None

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def discount_name(self):
        return self._discount_name

    @discount_name.setter
    def discount_name(self, value):
        self._discount_name = value
    @property
    def discount_page_link(self):
        return self._discount_page_link

    @discount_page_link.setter
    def discount_page_link(self, value):
        self._discount_page_link = value
    @property
    def discount_quantity(self):
        return self._discount_quantity

    @discount_quantity.setter
    def discount_quantity(self, value):
        self._discount_quantity = value
    @property
    def external_discount_id(self):
        return self._external_discount_id

    @external_discount_id.setter
    def external_discount_id(self, value):
        self._external_discount_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.discount_name:
            if hasattr(self.discount_name, 'to_alipay_dict'):
                params['discount_name'] = self.discount_name.to_alipay_dict()
            else:
                params['discount_name'] = self.discount_name
        if self.discount_page_link:
            if hasattr(self.discount_page_link, 'to_alipay_dict'):
                params['discount_page_link'] = self.discount_page_link.to_alipay_dict()
            else:
                params['discount_page_link'] = self.discount_page_link
        if self.discount_quantity:
            if hasattr(self.discount_quantity, 'to_alipay_dict'):
                params['discount_quantity'] = self.discount_quantity.to_alipay_dict()
            else:
                params['discount_quantity'] = self.discount_quantity
        if self.external_discount_id:
            if hasattr(self.external_discount_id, 'to_alipay_dict'):
                params['external_discount_id'] = self.external_discount_id.to_alipay_dict()
            else:
                params['external_discount_id'] = self.external_discount_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiscountInfoData()
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'discount_name' in d:
            o.discount_name = d['discount_name']
        if 'discount_page_link' in d:
            o.discount_page_link = d['discount_page_link']
        if 'discount_quantity' in d:
            o.discount_quantity = d['discount_quantity']
        if 'external_discount_id' in d:
            o.external_discount_id = d['external_discount_id']
        return o


