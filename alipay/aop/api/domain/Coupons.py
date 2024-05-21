#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Coupons(object):

    def __init__(self):
        self._activity_code = None
        self._amount = None
        self._coupon_code = None
        self._coupon_type = None
        self._discount = None
        self._end_time = None
        self._start_time = None
        self._use_threshold = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def coupon_code(self):
        return self._coupon_code

    @coupon_code.setter
    def coupon_code(self, value):
        self._coupon_code = value
    @property
    def coupon_type(self):
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, value):
        self._coupon_type = value
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def use_threshold(self):
        return self._use_threshold

    @use_threshold.setter
    def use_threshold(self, value):
        self._use_threshold = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.coupon_code:
            if hasattr(self.coupon_code, 'to_alipay_dict'):
                params['coupon_code'] = self.coupon_code.to_alipay_dict()
            else:
                params['coupon_code'] = self.coupon_code
        if self.coupon_type:
            if hasattr(self.coupon_type, 'to_alipay_dict'):
                params['coupon_type'] = self.coupon_type.to_alipay_dict()
            else:
                params['coupon_type'] = self.coupon_type
        if self.discount:
            if hasattr(self.discount, 'to_alipay_dict'):
                params['discount'] = self.discount.to_alipay_dict()
            else:
                params['discount'] = self.discount
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.use_threshold:
            if hasattr(self.use_threshold, 'to_alipay_dict'):
                params['use_threshold'] = self.use_threshold.to_alipay_dict()
            else:
                params['use_threshold'] = self.use_threshold
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Coupons()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'amount' in d:
            o.amount = d['amount']
        if 'coupon_code' in d:
            o.coupon_code = d['coupon_code']
        if 'coupon_type' in d:
            o.coupon_type = d['coupon_type']
        if 'discount' in d:
            o.discount = d['discount']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'use_threshold' in d:
            o.use_threshold = d['use_threshold']
        return o


