#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WelfareForestPersonWaterDTO(object):

    def __init__(self):
        self._user_water_count = None
        self._user_water_placing = None
        self._user_water_sum = None

    @property
    def user_water_count(self):
        return self._user_water_count

    @user_water_count.setter
    def user_water_count(self, value):
        self._user_water_count = value
    @property
    def user_water_placing(self):
        return self._user_water_placing

    @user_water_placing.setter
    def user_water_placing(self, value):
        self._user_water_placing = value
    @property
    def user_water_sum(self):
        return self._user_water_sum

    @user_water_sum.setter
    def user_water_sum(self, value):
        self._user_water_sum = value


    def to_alipay_dict(self):
        params = dict()
        if self.user_water_count:
            if hasattr(self.user_water_count, 'to_alipay_dict'):
                params['user_water_count'] = self.user_water_count.to_alipay_dict()
            else:
                params['user_water_count'] = self.user_water_count
        if self.user_water_placing:
            if hasattr(self.user_water_placing, 'to_alipay_dict'):
                params['user_water_placing'] = self.user_water_placing.to_alipay_dict()
            else:
                params['user_water_placing'] = self.user_water_placing
        if self.user_water_sum:
            if hasattr(self.user_water_sum, 'to_alipay_dict'):
                params['user_water_sum'] = self.user_water_sum.to_alipay_dict()
            else:
                params['user_water_sum'] = self.user_water_sum
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WelfareForestPersonWaterDTO()
        if 'user_water_count' in d:
            o.user_water_count = d['user_water_count']
        if 'user_water_placing' in d:
            o.user_water_placing = d['user_water_placing']
        if 'user_water_sum' in d:
            o.user_water_sum = d['user_water_sum']
        return o


