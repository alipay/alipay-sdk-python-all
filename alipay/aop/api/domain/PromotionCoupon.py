#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromotionCoupon(object):

    def __init__(self):
        self._amount_off = None
        self._coupon_id = None
        self._duration = None
        self._duration_in_iterations = None
        self._name = None
        self._percent_off = None
        self._redeem_by = None

    @property
    def amount_off(self):
        return self._amount_off

    @amount_off.setter
    def amount_off(self, value):
        self._amount_off = value
    @property
    def coupon_id(self):
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, value):
        self._coupon_id = value
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def duration_in_iterations(self):
        return self._duration_in_iterations

    @duration_in_iterations.setter
    def duration_in_iterations(self, value):
        self._duration_in_iterations = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def percent_off(self):
        return self._percent_off

    @percent_off.setter
    def percent_off(self, value):
        self._percent_off = value
    @property
    def redeem_by(self):
        return self._redeem_by

    @redeem_by.setter
    def redeem_by(self, value):
        self._redeem_by = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_off:
            if hasattr(self.amount_off, 'to_alipay_dict'):
                params['amount_off'] = self.amount_off.to_alipay_dict()
            else:
                params['amount_off'] = self.amount_off
        if self.coupon_id:
            if hasattr(self.coupon_id, 'to_alipay_dict'):
                params['coupon_id'] = self.coupon_id.to_alipay_dict()
            else:
                params['coupon_id'] = self.coupon_id
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.duration_in_iterations:
            if hasattr(self.duration_in_iterations, 'to_alipay_dict'):
                params['duration_in_iterations'] = self.duration_in_iterations.to_alipay_dict()
            else:
                params['duration_in_iterations'] = self.duration_in_iterations
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.percent_off:
            if hasattr(self.percent_off, 'to_alipay_dict'):
                params['percent_off'] = self.percent_off.to_alipay_dict()
            else:
                params['percent_off'] = self.percent_off
        if self.redeem_by:
            if hasattr(self.redeem_by, 'to_alipay_dict'):
                params['redeem_by'] = self.redeem_by.to_alipay_dict()
            else:
                params['redeem_by'] = self.redeem_by
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromotionCoupon()
        if 'amount_off' in d:
            o.amount_off = d['amount_off']
        if 'coupon_id' in d:
            o.coupon_id = d['coupon_id']
        if 'duration' in d:
            o.duration = d['duration']
        if 'duration_in_iterations' in d:
            o.duration_in_iterations = d['duration_in_iterations']
        if 'name' in d:
            o.name = d['name']
        if 'percent_off' in d:
            o.percent_off = d['percent_off']
        if 'redeem_by' in d:
            o.redeem_by = d['redeem_by']
        return o


