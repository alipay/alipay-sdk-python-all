#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsMktCouponDTO(object):

    def __init__(self):
        self._asset_id = None
        self._coupon_id = None
        self._coupon_type = None
        self._coupon_value = None
        self._recommend = None
        self._use_end_time = None
        self._use_rule = None
        self._use_start_time = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
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
    @property
    def recommend(self):
        return self._recommend

    @recommend.setter
    def recommend(self, value):
        self._recommend = value
    @property
    def use_end_time(self):
        return self._use_end_time

    @use_end_time.setter
    def use_end_time(self, value):
        self._use_end_time = value
    @property
    def use_rule(self):
        return self._use_rule

    @use_rule.setter
    def use_rule(self, value):
        self._use_rule = value
    @property
    def use_start_time(self):
        return self._use_start_time

    @use_start_time.setter
    def use_start_time(self, value):
        self._use_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
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
        if self.recommend:
            if hasattr(self.recommend, 'to_alipay_dict'):
                params['recommend'] = self.recommend.to_alipay_dict()
            else:
                params['recommend'] = self.recommend
        if self.use_end_time:
            if hasattr(self.use_end_time, 'to_alipay_dict'):
                params['use_end_time'] = self.use_end_time.to_alipay_dict()
            else:
                params['use_end_time'] = self.use_end_time
        if self.use_rule:
            if hasattr(self.use_rule, 'to_alipay_dict'):
                params['use_rule'] = self.use_rule.to_alipay_dict()
            else:
                params['use_rule'] = self.use_rule
        if self.use_start_time:
            if hasattr(self.use_start_time, 'to_alipay_dict'):
                params['use_start_time'] = self.use_start_time.to_alipay_dict()
            else:
                params['use_start_time'] = self.use_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsMktCouponDTO()
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'coupon_id' in d:
            o.coupon_id = d['coupon_id']
        if 'coupon_type' in d:
            o.coupon_type = d['coupon_type']
        if 'coupon_value' in d:
            o.coupon_value = d['coupon_value']
        if 'recommend' in d:
            o.recommend = d['recommend']
        if 'use_end_time' in d:
            o.use_end_time = d['use_end_time']
        if 'use_rule' in d:
            o.use_rule = d['use_rule']
        if 'use_start_time' in d:
            o.use_start_time = d['use_start_time']
        return o


