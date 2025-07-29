#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SupplementCategoryInfo(object):

    def __init__(self):
        self._supplement_category = None
        self._supplement_payment_amt = None

    @property
    def supplement_category(self):
        return self._supplement_category

    @supplement_category.setter
    def supplement_category(self, value):
        self._supplement_category = value
    @property
    def supplement_payment_amt(self):
        return self._supplement_payment_amt

    @supplement_payment_amt.setter
    def supplement_payment_amt(self, value):
        self._supplement_payment_amt = value


    def to_alipay_dict(self):
        params = dict()
        if self.supplement_category:
            if hasattr(self.supplement_category, 'to_alipay_dict'):
                params['supplement_category'] = self.supplement_category.to_alipay_dict()
            else:
                params['supplement_category'] = self.supplement_category
        if self.supplement_payment_amt:
            if hasattr(self.supplement_payment_amt, 'to_alipay_dict'):
                params['supplement_payment_amt'] = self.supplement_payment_amt.to_alipay_dict()
            else:
                params['supplement_payment_amt'] = self.supplement_payment_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SupplementCategoryInfo()
        if 'supplement_category' in d:
            o.supplement_category = d['supplement_category']
        if 'supplement_payment_amt' in d:
            o.supplement_payment_amt = d['supplement_payment_amt']
        return o


