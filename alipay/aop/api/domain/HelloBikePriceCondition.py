#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HelloBikePriceCondition(object):

    def __init__(self):
        self._card_type_left = None
        self._card_type_right = None
        self._coefficient_left = None
        self._coefficient_right = None

    @property
    def card_type_left(self):
        return self._card_type_left

    @card_type_left.setter
    def card_type_left(self, value):
        self._card_type_left = value
    @property
    def card_type_right(self):
        return self._card_type_right

    @card_type_right.setter
    def card_type_right(self, value):
        self._card_type_right = value
    @property
    def coefficient_left(self):
        return self._coefficient_left

    @coefficient_left.setter
    def coefficient_left(self, value):
        self._coefficient_left = value
    @property
    def coefficient_right(self):
        return self._coefficient_right

    @coefficient_right.setter
    def coefficient_right(self, value):
        self._coefficient_right = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_type_left:
            if hasattr(self.card_type_left, 'to_alipay_dict'):
                params['card_type_left'] = self.card_type_left.to_alipay_dict()
            else:
                params['card_type_left'] = self.card_type_left
        if self.card_type_right:
            if hasattr(self.card_type_right, 'to_alipay_dict'):
                params['card_type_right'] = self.card_type_right.to_alipay_dict()
            else:
                params['card_type_right'] = self.card_type_right
        if self.coefficient_left:
            if hasattr(self.coefficient_left, 'to_alipay_dict'):
                params['coefficient_left'] = self.coefficient_left.to_alipay_dict()
            else:
                params['coefficient_left'] = self.coefficient_left
        if self.coefficient_right:
            if hasattr(self.coefficient_right, 'to_alipay_dict'):
                params['coefficient_right'] = self.coefficient_right.to_alipay_dict()
            else:
                params['coefficient_right'] = self.coefficient_right
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HelloBikePriceCondition()
        if 'card_type_left' in d:
            o.card_type_left = d['card_type_left']
        if 'card_type_right' in d:
            o.card_type_right = d['card_type_right']
        if 'coefficient_left' in d:
            o.coefficient_left = d['coefficient_left']
        if 'coefficient_right' in d:
            o.coefficient_right = d['coefficient_right']
        return o


