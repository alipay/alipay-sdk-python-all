#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MallDiscountDetail(object):

    def __init__(self):
        self._discount_amount = None
        self._discount_desc = None
        self._discount_type = None
        self._id = None
        self._name = None
        self._purchased = None

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def discount_desc(self):
        return self._discount_desc

    @discount_desc.setter
    def discount_desc(self, value):
        if isinstance(value, list):
            self._discount_desc = list()
            for i in value:
                self._discount_desc.append(i)
    @property
    def discount_type(self):
        return self._discount_type

    @discount_type.setter
    def discount_type(self, value):
        self._discount_type = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def purchased(self):
        return self._purchased

    @purchased.setter
    def purchased(self, value):
        self._purchased = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.discount_desc:
            if isinstance(self.discount_desc, list):
                for i in range(0, len(self.discount_desc)):
                    element = self.discount_desc[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_desc[i] = element.to_alipay_dict()
            if hasattr(self.discount_desc, 'to_alipay_dict'):
                params['discount_desc'] = self.discount_desc.to_alipay_dict()
            else:
                params['discount_desc'] = self.discount_desc
        if self.discount_type:
            if hasattr(self.discount_type, 'to_alipay_dict'):
                params['discount_type'] = self.discount_type.to_alipay_dict()
            else:
                params['discount_type'] = self.discount_type
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.purchased:
            if hasattr(self.purchased, 'to_alipay_dict'):
                params['purchased'] = self.purchased.to_alipay_dict()
            else:
                params['purchased'] = self.purchased
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MallDiscountDetail()
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'discount_desc' in d:
            o.discount_desc = d['discount_desc']
        if 'discount_type' in d:
            o.discount_type = d['discount_type']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'purchased' in d:
            o.purchased = d['purchased']
        return o


