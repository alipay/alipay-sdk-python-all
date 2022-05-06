#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChangedContent(object):

    def __init__(self):
        self._expire_deferral_after_expire_time = None
        self._expire_deferral_sum_deferral_time = None
        self._expire_deferral_sum_deferral_time_unit = None
        self._expire_deferral_use_time = None

    @property
    def expire_deferral_after_expire_time(self):
        return self._expire_deferral_after_expire_time

    @expire_deferral_after_expire_time.setter
    def expire_deferral_after_expire_time(self, value):
        self._expire_deferral_after_expire_time = value
    @property
    def expire_deferral_sum_deferral_time(self):
        return self._expire_deferral_sum_deferral_time

    @expire_deferral_sum_deferral_time.setter
    def expire_deferral_sum_deferral_time(self, value):
        self._expire_deferral_sum_deferral_time = value
    @property
    def expire_deferral_sum_deferral_time_unit(self):
        return self._expire_deferral_sum_deferral_time_unit

    @expire_deferral_sum_deferral_time_unit.setter
    def expire_deferral_sum_deferral_time_unit(self, value):
        self._expire_deferral_sum_deferral_time_unit = value
    @property
    def expire_deferral_use_time(self):
        return self._expire_deferral_use_time

    @expire_deferral_use_time.setter
    def expire_deferral_use_time(self, value):
        self._expire_deferral_use_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.expire_deferral_after_expire_time:
            if hasattr(self.expire_deferral_after_expire_time, 'to_alipay_dict'):
                params['expire_deferral_after_expire_time'] = self.expire_deferral_after_expire_time.to_alipay_dict()
            else:
                params['expire_deferral_after_expire_time'] = self.expire_deferral_after_expire_time
        if self.expire_deferral_sum_deferral_time:
            if hasattr(self.expire_deferral_sum_deferral_time, 'to_alipay_dict'):
                params['expire_deferral_sum_deferral_time'] = self.expire_deferral_sum_deferral_time.to_alipay_dict()
            else:
                params['expire_deferral_sum_deferral_time'] = self.expire_deferral_sum_deferral_time
        if self.expire_deferral_sum_deferral_time_unit:
            if hasattr(self.expire_deferral_sum_deferral_time_unit, 'to_alipay_dict'):
                params['expire_deferral_sum_deferral_time_unit'] = self.expire_deferral_sum_deferral_time_unit.to_alipay_dict()
            else:
                params['expire_deferral_sum_deferral_time_unit'] = self.expire_deferral_sum_deferral_time_unit
        if self.expire_deferral_use_time:
            if hasattr(self.expire_deferral_use_time, 'to_alipay_dict'):
                params['expire_deferral_use_time'] = self.expire_deferral_use_time.to_alipay_dict()
            else:
                params['expire_deferral_use_time'] = self.expire_deferral_use_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChangedContent()
        if 'expire_deferral_after_expire_time' in d:
            o.expire_deferral_after_expire_time = d['expire_deferral_after_expire_time']
        if 'expire_deferral_sum_deferral_time' in d:
            o.expire_deferral_sum_deferral_time = d['expire_deferral_sum_deferral_time']
        if 'expire_deferral_sum_deferral_time_unit' in d:
            o.expire_deferral_sum_deferral_time_unit = d['expire_deferral_sum_deferral_time_unit']
        if 'expire_deferral_use_time' in d:
            o.expire_deferral_use_time = d['expire_deferral_use_time']
        return o


