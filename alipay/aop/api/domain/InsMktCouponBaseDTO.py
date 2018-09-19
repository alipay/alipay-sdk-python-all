#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsMktCouponBaseDTO(object):

    def __init__(self):
        self._coupon_id = None
        self._coupon_type = None
        self._coupon_value = None

    @property
    def coupon_id(self):
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, value):
        self._coupon_id = value
    @property
    def coupon_type(self):
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, value):
        self._coupon_type = value
    @property
    def coupon_value(self):
        return self._coupon_value

    @coupon_value.setter
    def coupon_value(self, value):
        self._coupon_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.coupon_id:
            if hasattr(self.coupon_id, 'to_alipay_dict'):
                params['coupon_id'] = self.coupon_id.to_alipay_dict()
            else:
                params['coupon_id'] = self.coupon_id
        if self.coupon_type:
            if hasattr(self.coupon_type, 'to_alipay_dict'):
                params['coupon_type'] = self.coupon_type.to_alipay_dict()
            else:
                params['coupon_type'] = self.coupon_type
        if self.coupon_value:
            if hasattr(self.coupon_value, 'to_alipay_dict'):
                params['coupon_value'] = self.coupon_value.to_alipay_dict()
            else:
                params['coupon_value'] = self.coupon_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsMktCouponBaseDTO()
        if 'coupon_id' in d:
            o.coupon_id = d['coupon_id']
        if 'coupon_type' in d:
            o.coupon_type = d['coupon_type']
        if 'coupon_value' in d:
            o.coupon_value = d['coupon_value']
        return o


