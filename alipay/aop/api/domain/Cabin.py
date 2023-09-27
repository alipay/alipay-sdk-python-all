#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Cabin(object):

    def __init__(self):
        self._adult_discount_price = None
        self._adult_price = None
        self._cabin_code = None
        self._cabin_discount = None
        self._cabin_name = None
        self._child_price = None
        self._discount_tag = None
        self._infant_price = None
        self._meal = None
        self._ticket_count = None

    @property
    def adult_discount_price(self):
        return self._adult_discount_price

    @adult_discount_price.setter
    def adult_discount_price(self, value):
        self._adult_discount_price = value
    @property
    def adult_price(self):
        return self._adult_price

    @adult_price.setter
    def adult_price(self, value):
        self._adult_price = value
    @property
    def cabin_code(self):
        return self._cabin_code

    @cabin_code.setter
    def cabin_code(self, value):
        self._cabin_code = value
    @property
    def cabin_discount(self):
        return self._cabin_discount

    @cabin_discount.setter
    def cabin_discount(self, value):
        self._cabin_discount = value
    @property
    def cabin_name(self):
        return self._cabin_name

    @cabin_name.setter
    def cabin_name(self, value):
        self._cabin_name = value
    @property
    def child_price(self):
        return self._child_price

    @child_price.setter
    def child_price(self, value):
        self._child_price = value
    @property
    def discount_tag(self):
        return self._discount_tag

    @discount_tag.setter
    def discount_tag(self, value):
        self._discount_tag = value
    @property
    def infant_price(self):
        return self._infant_price

    @infant_price.setter
    def infant_price(self, value):
        self._infant_price = value
    @property
    def meal(self):
        return self._meal

    @meal.setter
    def meal(self, value):
        self._meal = value
    @property
    def ticket_count(self):
        return self._ticket_count

    @ticket_count.setter
    def ticket_count(self, value):
        self._ticket_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.adult_discount_price:
            if hasattr(self.adult_discount_price, 'to_alipay_dict'):
                params['adult_discount_price'] = self.adult_discount_price.to_alipay_dict()
            else:
                params['adult_discount_price'] = self.adult_discount_price
        if self.adult_price:
            if hasattr(self.adult_price, 'to_alipay_dict'):
                params['adult_price'] = self.adult_price.to_alipay_dict()
            else:
                params['adult_price'] = self.adult_price
        if self.cabin_code:
            if hasattr(self.cabin_code, 'to_alipay_dict'):
                params['cabin_code'] = self.cabin_code.to_alipay_dict()
            else:
                params['cabin_code'] = self.cabin_code
        if self.cabin_discount:
            if hasattr(self.cabin_discount, 'to_alipay_dict'):
                params['cabin_discount'] = self.cabin_discount.to_alipay_dict()
            else:
                params['cabin_discount'] = self.cabin_discount
        if self.cabin_name:
            if hasattr(self.cabin_name, 'to_alipay_dict'):
                params['cabin_name'] = self.cabin_name.to_alipay_dict()
            else:
                params['cabin_name'] = self.cabin_name
        if self.child_price:
            if hasattr(self.child_price, 'to_alipay_dict'):
                params['child_price'] = self.child_price.to_alipay_dict()
            else:
                params['child_price'] = self.child_price
        if self.discount_tag:
            if hasattr(self.discount_tag, 'to_alipay_dict'):
                params['discount_tag'] = self.discount_tag.to_alipay_dict()
            else:
                params['discount_tag'] = self.discount_tag
        if self.infant_price:
            if hasattr(self.infant_price, 'to_alipay_dict'):
                params['infant_price'] = self.infant_price.to_alipay_dict()
            else:
                params['infant_price'] = self.infant_price
        if self.meal:
            if hasattr(self.meal, 'to_alipay_dict'):
                params['meal'] = self.meal.to_alipay_dict()
            else:
                params['meal'] = self.meal
        if self.ticket_count:
            if hasattr(self.ticket_count, 'to_alipay_dict'):
                params['ticket_count'] = self.ticket_count.to_alipay_dict()
            else:
                params['ticket_count'] = self.ticket_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Cabin()
        if 'adult_discount_price' in d:
            o.adult_discount_price = d['adult_discount_price']
        if 'adult_price' in d:
            o.adult_price = d['adult_price']
        if 'cabin_code' in d:
            o.cabin_code = d['cabin_code']
        if 'cabin_discount' in d:
            o.cabin_discount = d['cabin_discount']
        if 'cabin_name' in d:
            o.cabin_name = d['cabin_name']
        if 'child_price' in d:
            o.child_price = d['child_price']
        if 'discount_tag' in d:
            o.discount_tag = d['discount_tag']
        if 'infant_price' in d:
            o.infant_price = d['infant_price']
        if 'meal' in d:
            o.meal = d['meal']
        if 'ticket_count' in d:
            o.ticket_count = d['ticket_count']
        return o


