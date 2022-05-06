#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GoodExpirationListDTO(object):

    def __init__(self):
        self._good_effective_duration = None
        self._good_expiration_time = None
        self._good_prd_time = None

    @property
    def good_effective_duration(self):
        return self._good_effective_duration

    @good_effective_duration.setter
    def good_effective_duration(self, value):
        self._good_effective_duration = value
    @property
    def good_expiration_time(self):
        return self._good_expiration_time

    @good_expiration_time.setter
    def good_expiration_time(self, value):
        self._good_expiration_time = value
    @property
    def good_prd_time(self):
        return self._good_prd_time

    @good_prd_time.setter
    def good_prd_time(self, value):
        self._good_prd_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.good_effective_duration:
            if hasattr(self.good_effective_duration, 'to_alipay_dict'):
                params['good_effective_duration'] = self.good_effective_duration.to_alipay_dict()
            else:
                params['good_effective_duration'] = self.good_effective_duration
        if self.good_expiration_time:
            if hasattr(self.good_expiration_time, 'to_alipay_dict'):
                params['good_expiration_time'] = self.good_expiration_time.to_alipay_dict()
            else:
                params['good_expiration_time'] = self.good_expiration_time
        if self.good_prd_time:
            if hasattr(self.good_prd_time, 'to_alipay_dict'):
                params['good_prd_time'] = self.good_prd_time.to_alipay_dict()
            else:
                params['good_prd_time'] = self.good_prd_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GoodExpirationListDTO()
        if 'good_effective_duration' in d:
            o.good_effective_duration = d['good_effective_duration']
        if 'good_expiration_time' in d:
            o.good_expiration_time = d['good_expiration_time']
        if 'good_prd_time' in d:
            o.good_prd_time = d['good_prd_time']
        return o


