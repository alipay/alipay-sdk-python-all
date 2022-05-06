#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DesignatedDrivingDynamicPrice(object):

    def __init__(self):
        self._dynamic_fee = None
        self._dynamic_rate = None
        self._dynamic_reason = None
        self._dynamic_title = None
        self._fee_max = None
        self._fee_type = None

    @property
    def dynamic_fee(self):
        return self._dynamic_fee

    @dynamic_fee.setter
    def dynamic_fee(self, value):
        self._dynamic_fee = value
    @property
    def dynamic_rate(self):
        return self._dynamic_rate

    @dynamic_rate.setter
    def dynamic_rate(self, value):
        self._dynamic_rate = value
    @property
    def dynamic_reason(self):
        return self._dynamic_reason

    @dynamic_reason.setter
    def dynamic_reason(self, value):
        self._dynamic_reason = value
    @property
    def dynamic_title(self):
        return self._dynamic_title

    @dynamic_title.setter
    def dynamic_title(self, value):
        self._dynamic_title = value
    @property
    def fee_max(self):
        return self._fee_max

    @fee_max.setter
    def fee_max(self, value):
        self._fee_max = value
    @property
    def fee_type(self):
        return self._fee_type

    @fee_type.setter
    def fee_type(self, value):
        self._fee_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.dynamic_fee:
            if hasattr(self.dynamic_fee, 'to_alipay_dict'):
                params['dynamic_fee'] = self.dynamic_fee.to_alipay_dict()
            else:
                params['dynamic_fee'] = self.dynamic_fee
        if self.dynamic_rate:
            if hasattr(self.dynamic_rate, 'to_alipay_dict'):
                params['dynamic_rate'] = self.dynamic_rate.to_alipay_dict()
            else:
                params['dynamic_rate'] = self.dynamic_rate
        if self.dynamic_reason:
            if hasattr(self.dynamic_reason, 'to_alipay_dict'):
                params['dynamic_reason'] = self.dynamic_reason.to_alipay_dict()
            else:
                params['dynamic_reason'] = self.dynamic_reason
        if self.dynamic_title:
            if hasattr(self.dynamic_title, 'to_alipay_dict'):
                params['dynamic_title'] = self.dynamic_title.to_alipay_dict()
            else:
                params['dynamic_title'] = self.dynamic_title
        if self.fee_max:
            if hasattr(self.fee_max, 'to_alipay_dict'):
                params['fee_max'] = self.fee_max.to_alipay_dict()
            else:
                params['fee_max'] = self.fee_max
        if self.fee_type:
            if hasattr(self.fee_type, 'to_alipay_dict'):
                params['fee_type'] = self.fee_type.to_alipay_dict()
            else:
                params['fee_type'] = self.fee_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DesignatedDrivingDynamicPrice()
        if 'dynamic_fee' in d:
            o.dynamic_fee = d['dynamic_fee']
        if 'dynamic_rate' in d:
            o.dynamic_rate = d['dynamic_rate']
        if 'dynamic_reason' in d:
            o.dynamic_reason = d['dynamic_reason']
        if 'dynamic_title' in d:
            o.dynamic_title = d['dynamic_title']
        if 'fee_max' in d:
            o.fee_max = d['fee_max']
        if 'fee_type' in d:
            o.fee_type = d['fee_type']
        return o


