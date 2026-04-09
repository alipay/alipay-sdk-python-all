#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubPrizeDiscountInfo(object):

    def __init__(self):
        self._exist_discount_threshold = None
        self._reduce_amount = None
        self._threshold_amount = None

    @property
    def exist_discount_threshold(self):
        return self._exist_discount_threshold

    @exist_discount_threshold.setter
    def exist_discount_threshold(self, value):
        self._exist_discount_threshold = value
    @property
    def reduce_amount(self):
        return self._reduce_amount

    @reduce_amount.setter
    def reduce_amount(self, value):
        self._reduce_amount = value
    @property
    def threshold_amount(self):
        return self._threshold_amount

    @threshold_amount.setter
    def threshold_amount(self, value):
        self._threshold_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.exist_discount_threshold:
            if hasattr(self.exist_discount_threshold, 'to_alipay_dict'):
                params['exist_discount_threshold'] = self.exist_discount_threshold.to_alipay_dict()
            else:
                params['exist_discount_threshold'] = self.exist_discount_threshold
        if self.reduce_amount:
            if hasattr(self.reduce_amount, 'to_alipay_dict'):
                params['reduce_amount'] = self.reduce_amount.to_alipay_dict()
            else:
                params['reduce_amount'] = self.reduce_amount
        if self.threshold_amount:
            if hasattr(self.threshold_amount, 'to_alipay_dict'):
                params['threshold_amount'] = self.threshold_amount.to_alipay_dict()
            else:
                params['threshold_amount'] = self.threshold_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubPrizeDiscountInfo()
        if 'exist_discount_threshold' in d:
            o.exist_discount_threshold = d['exist_discount_threshold']
        if 'reduce_amount' in d:
            o.reduce_amount = d['reduce_amount']
        if 'threshold_amount' in d:
            o.threshold_amount = d['threshold_amount']
        return o


