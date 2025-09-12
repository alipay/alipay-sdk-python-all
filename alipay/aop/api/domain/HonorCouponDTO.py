#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HonorCouponDTO(object):

    def __init__(self):
        self._coupon_name = None
        self._coupon_no = None
        self._coupon_type = None
        self._end_time = None
        self._receive_time = None
        self._select_status = None
        self._start_time = None
        self._status = None
        self._unusable_reason = None
        self._use_rules = None
        self._used_time = None

    @property
    def coupon_name(self):
        return self._coupon_name

    @coupon_name.setter
    def coupon_name(self, value):
        self._coupon_name = value
    @property
    def coupon_no(self):
        return self._coupon_no

    @coupon_no.setter
    def coupon_no(self, value):
        self._coupon_no = value
    @property
    def coupon_type(self):
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, value):
        self._coupon_type = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def receive_time(self):
        return self._receive_time

    @receive_time.setter
    def receive_time(self, value):
        self._receive_time = value
    @property
    def select_status(self):
        return self._select_status

    @select_status.setter
    def select_status(self, value):
        self._select_status = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def unusable_reason(self):
        return self._unusable_reason

    @unusable_reason.setter
    def unusable_reason(self, value):
        self._unusable_reason = value
    @property
    def use_rules(self):
        return self._use_rules

    @use_rules.setter
    def use_rules(self, value):
        if isinstance(value, list):
            self._use_rules = list()
            for i in value:
                self._use_rules.append(i)
    @property
    def used_time(self):
        return self._used_time

    @used_time.setter
    def used_time(self, value):
        self._used_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.coupon_name:
            if hasattr(self.coupon_name, 'to_alipay_dict'):
                params['coupon_name'] = self.coupon_name.to_alipay_dict()
            else:
                params['coupon_name'] = self.coupon_name
        if self.coupon_no:
            if hasattr(self.coupon_no, 'to_alipay_dict'):
                params['coupon_no'] = self.coupon_no.to_alipay_dict()
            else:
                params['coupon_no'] = self.coupon_no
        if self.coupon_type:
            if hasattr(self.coupon_type, 'to_alipay_dict'):
                params['coupon_type'] = self.coupon_type.to_alipay_dict()
            else:
                params['coupon_type'] = self.coupon_type
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.receive_time:
            if hasattr(self.receive_time, 'to_alipay_dict'):
                params['receive_time'] = self.receive_time.to_alipay_dict()
            else:
                params['receive_time'] = self.receive_time
        if self.select_status:
            if hasattr(self.select_status, 'to_alipay_dict'):
                params['select_status'] = self.select_status.to_alipay_dict()
            else:
                params['select_status'] = self.select_status
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.unusable_reason:
            if hasattr(self.unusable_reason, 'to_alipay_dict'):
                params['unusable_reason'] = self.unusable_reason.to_alipay_dict()
            else:
                params['unusable_reason'] = self.unusable_reason
        if self.use_rules:
            if isinstance(self.use_rules, list):
                for i in range(0, len(self.use_rules)):
                    element = self.use_rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.use_rules[i] = element.to_alipay_dict()
            if hasattr(self.use_rules, 'to_alipay_dict'):
                params['use_rules'] = self.use_rules.to_alipay_dict()
            else:
                params['use_rules'] = self.use_rules
        if self.used_time:
            if hasattr(self.used_time, 'to_alipay_dict'):
                params['used_time'] = self.used_time.to_alipay_dict()
            else:
                params['used_time'] = self.used_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HonorCouponDTO()
        if 'coupon_name' in d:
            o.coupon_name = d['coupon_name']
        if 'coupon_no' in d:
            o.coupon_no = d['coupon_no']
        if 'coupon_type' in d:
            o.coupon_type = d['coupon_type']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'receive_time' in d:
            o.receive_time = d['receive_time']
        if 'select_status' in d:
            o.select_status = d['select_status']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'unusable_reason' in d:
            o.unusable_reason = d['unusable_reason']
        if 'use_rules' in d:
            o.use_rules = d['use_rules']
        if 'used_time' in d:
            o.used_time = d['used_time']
        return o


