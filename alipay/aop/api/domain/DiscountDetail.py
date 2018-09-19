#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DiscountDetail(object):

    def __init__(self):
        self._discount_amount = None
        self._discount_desc = None
        self._discount_type = None
        self._id = None
        self._is_hit = None
        self._is_purchased = None
        self._name = None

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
    def is_hit(self):
        return self._is_hit

    @is_hit.setter
    def is_hit(self, value):
        self._is_hit = value
    @property
    def is_purchased(self):
        return self._is_purchased

    @is_purchased.setter
    def is_purchased(self, value):
        self._is_purchased = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


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
        if self.is_hit:
            if hasattr(self.is_hit, 'to_alipay_dict'):
                params['is_hit'] = self.is_hit.to_alipay_dict()
            else:
                params['is_hit'] = self.is_hit
        if self.is_purchased:
            if hasattr(self.is_purchased, 'to_alipay_dict'):
                params['is_purchased'] = self.is_purchased.to_alipay_dict()
            else:
                params['is_purchased'] = self.is_purchased
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiscountDetail()
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'discount_desc' in d:
            o.discount_desc = d['discount_desc']
        if 'discount_type' in d:
            o.discount_type = d['discount_type']
        if 'id' in d:
            o.id = d['id']
        if 'is_hit' in d:
            o.is_hit = d['is_hit']
        if 'is_purchased' in d:
            o.is_purchased = d['is_purchased']
        if 'name' in d:
            o.name = d['name']
        return o


