#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CouponEffectTime(object):

    def __init__(self):
        self._coupon_absolutely_begin_time = None
        self._coupon_absolutely_end_time = None
        self._coupon_available_period_type = None
        self._coupon_relative_begin_rounding_type = None
        self._coupon_relative_begin_value = None
        self._coupon_relative_end_rounding_type = None
        self._coupon_relative_end_value = None

    @property
    def coupon_absolutely_begin_time(self):
        return self._coupon_absolutely_begin_time

    @coupon_absolutely_begin_time.setter
    def coupon_absolutely_begin_time(self, value):
        self._coupon_absolutely_begin_time = value
    @property
    def coupon_absolutely_end_time(self):
        return self._coupon_absolutely_end_time

    @coupon_absolutely_end_time.setter
    def coupon_absolutely_end_time(self, value):
        self._coupon_absolutely_end_time = value
    @property
    def coupon_available_period_type(self):
        return self._coupon_available_period_type

    @coupon_available_period_type.setter
    def coupon_available_period_type(self, value):
        self._coupon_available_period_type = value
    @property
    def coupon_relative_begin_rounding_type(self):
        return self._coupon_relative_begin_rounding_type

    @coupon_relative_begin_rounding_type.setter
    def coupon_relative_begin_rounding_type(self, value):
        self._coupon_relative_begin_rounding_type = value
    @property
    def coupon_relative_begin_value(self):
        return self._coupon_relative_begin_value

    @coupon_relative_begin_value.setter
    def coupon_relative_begin_value(self, value):
        self._coupon_relative_begin_value = value
    @property
    def coupon_relative_end_rounding_type(self):
        return self._coupon_relative_end_rounding_type

    @coupon_relative_end_rounding_type.setter
    def coupon_relative_end_rounding_type(self, value):
        self._coupon_relative_end_rounding_type = value
    @property
    def coupon_relative_end_value(self):
        return self._coupon_relative_end_value

    @coupon_relative_end_value.setter
    def coupon_relative_end_value(self, value):
        self._coupon_relative_end_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.coupon_absolutely_begin_time:
            if hasattr(self.coupon_absolutely_begin_time, 'to_alipay_dict'):
                params['coupon_absolutely_begin_time'] = self.coupon_absolutely_begin_time.to_alipay_dict()
            else:
                params['coupon_absolutely_begin_time'] = self.coupon_absolutely_begin_time
        if self.coupon_absolutely_end_time:
            if hasattr(self.coupon_absolutely_end_time, 'to_alipay_dict'):
                params['coupon_absolutely_end_time'] = self.coupon_absolutely_end_time.to_alipay_dict()
            else:
                params['coupon_absolutely_end_time'] = self.coupon_absolutely_end_time
        if self.coupon_available_period_type:
            if hasattr(self.coupon_available_period_type, 'to_alipay_dict'):
                params['coupon_available_period_type'] = self.coupon_available_period_type.to_alipay_dict()
            else:
                params['coupon_available_period_type'] = self.coupon_available_period_type
        if self.coupon_relative_begin_rounding_type:
            if hasattr(self.coupon_relative_begin_rounding_type, 'to_alipay_dict'):
                params['coupon_relative_begin_rounding_type'] = self.coupon_relative_begin_rounding_type.to_alipay_dict()
            else:
                params['coupon_relative_begin_rounding_type'] = self.coupon_relative_begin_rounding_type
        if self.coupon_relative_begin_value:
            if hasattr(self.coupon_relative_begin_value, 'to_alipay_dict'):
                params['coupon_relative_begin_value'] = self.coupon_relative_begin_value.to_alipay_dict()
            else:
                params['coupon_relative_begin_value'] = self.coupon_relative_begin_value
        if self.coupon_relative_end_rounding_type:
            if hasattr(self.coupon_relative_end_rounding_type, 'to_alipay_dict'):
                params['coupon_relative_end_rounding_type'] = self.coupon_relative_end_rounding_type.to_alipay_dict()
            else:
                params['coupon_relative_end_rounding_type'] = self.coupon_relative_end_rounding_type
        if self.coupon_relative_end_value:
            if hasattr(self.coupon_relative_end_value, 'to_alipay_dict'):
                params['coupon_relative_end_value'] = self.coupon_relative_end_value.to_alipay_dict()
            else:
                params['coupon_relative_end_value'] = self.coupon_relative_end_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CouponEffectTime()
        if 'coupon_absolutely_begin_time' in d:
            o.coupon_absolutely_begin_time = d['coupon_absolutely_begin_time']
        if 'coupon_absolutely_end_time' in d:
            o.coupon_absolutely_end_time = d['coupon_absolutely_end_time']
        if 'coupon_available_period_type' in d:
            o.coupon_available_period_type = d['coupon_available_period_type']
        if 'coupon_relative_begin_rounding_type' in d:
            o.coupon_relative_begin_rounding_type = d['coupon_relative_begin_rounding_type']
        if 'coupon_relative_begin_value' in d:
            o.coupon_relative_begin_value = d['coupon_relative_begin_value']
        if 'coupon_relative_end_rounding_type' in d:
            o.coupon_relative_end_rounding_type = d['coupon_relative_end_rounding_type']
        if 'coupon_relative_end_value' in d:
            o.coupon_relative_end_value = d['coupon_relative_end_value']
        return o


