#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromoInfo(object):

    def __init__(self):
        self._ceiling_amount = None
        self._reduction_amount = None
        self._reduction_ratio = None
        self._specified_amount = None

    @property
    def ceiling_amount(self):
        return self._ceiling_amount

    @ceiling_amount.setter
    def ceiling_amount(self, value):
        self._ceiling_amount = value
    @property
    def reduction_amount(self):
        return self._reduction_amount

    @reduction_amount.setter
    def reduction_amount(self, value):
        self._reduction_amount = value
    @property
    def reduction_ratio(self):
        return self._reduction_ratio

    @reduction_ratio.setter
    def reduction_ratio(self, value):
        self._reduction_ratio = value
    @property
    def specified_amount(self):
        return self._specified_amount

    @specified_amount.setter
    def specified_amount(self, value):
        self._specified_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.ceiling_amount:
            if hasattr(self.ceiling_amount, 'to_alipay_dict'):
                params['ceiling_amount'] = self.ceiling_amount.to_alipay_dict()
            else:
                params['ceiling_amount'] = self.ceiling_amount
        if self.reduction_amount:
            if hasattr(self.reduction_amount, 'to_alipay_dict'):
                params['reduction_amount'] = self.reduction_amount.to_alipay_dict()
            else:
                params['reduction_amount'] = self.reduction_amount
        if self.reduction_ratio:
            if hasattr(self.reduction_ratio, 'to_alipay_dict'):
                params['reduction_ratio'] = self.reduction_ratio.to_alipay_dict()
            else:
                params['reduction_ratio'] = self.reduction_ratio
        if self.specified_amount:
            if hasattr(self.specified_amount, 'to_alipay_dict'):
                params['specified_amount'] = self.specified_amount.to_alipay_dict()
            else:
                params['specified_amount'] = self.specified_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoInfo()
        if 'ceiling_amount' in d:
            o.ceiling_amount = d['ceiling_amount']
        if 'reduction_amount' in d:
            o.reduction_amount = d['reduction_amount']
        if 'reduction_ratio' in d:
            o.reduction_ratio = d['reduction_ratio']
        if 'specified_amount' in d:
            o.specified_amount = d['specified_amount']
        return o


