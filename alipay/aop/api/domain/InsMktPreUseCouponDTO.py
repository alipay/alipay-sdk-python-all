#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsMktPreUseCouponDTO(object):

    def __init__(self):
        self._asset_id = None
        self._coupon_id = None
        self._coupon_type = None
        self._coupon_value = None
        self._pre_use = None
        self._reason = None

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
    def pre_use(self):
        return self._pre_use

    @pre_use.setter
    def pre_use(self, value):
        self._pre_use = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value


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
        if self.pre_use:
            if hasattr(self.pre_use, 'to_alipay_dict'):
                params['pre_use'] = self.pre_use.to_alipay_dict()
            else:
                params['pre_use'] = self.pre_use
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsMktPreUseCouponDTO()
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'coupon_id' in d:
            o.coupon_id = d['coupon_id']
        if 'coupon_type' in d:
            o.coupon_type = d['coupon_type']
        if 'coupon_value' in d:
            o.coupon_value = d['coupon_value']
        if 'pre_use' in d:
            o.pre_use = d['pre_use']
        if 'reason' in d:
            o.reason = d['reason']
        return o


