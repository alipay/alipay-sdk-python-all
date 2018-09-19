#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DiscountModel(object):

    def __init__(self):
        self._term_discount = None
        self._term_no = None

    @property
    def term_discount(self):
        return self._term_discount

    @term_discount.setter
    def term_discount(self, value):
        self._term_discount = value
    @property
    def term_no(self):
        return self._term_no

    @term_no.setter
    def term_no(self, value):
        self._term_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.term_discount:
            if hasattr(self.term_discount, 'to_alipay_dict'):
                params['term_discount'] = self.term_discount.to_alipay_dict()
            else:
                params['term_discount'] = self.term_discount
        if self.term_no:
            if hasattr(self.term_no, 'to_alipay_dict'):
                params['term_no'] = self.term_no.to_alipay_dict()
            else:
                params['term_no'] = self.term_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiscountModel()
        if 'term_discount' in d:
            o.term_discount = d['term_discount']
        if 'term_no' in d:
            o.term_no = d['term_no']
        return o


