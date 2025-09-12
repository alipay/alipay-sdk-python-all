#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HonorTempLimitInfoDTO(object):

    def __init__(self):
        self._temp_available_limit = None
        self._temp_credit_limit = None
        self._temp_limit_valid_time = None

    @property
    def temp_available_limit(self):
        return self._temp_available_limit

    @temp_available_limit.setter
    def temp_available_limit(self, value):
        self._temp_available_limit = value
    @property
    def temp_credit_limit(self):
        return self._temp_credit_limit

    @temp_credit_limit.setter
    def temp_credit_limit(self, value):
        self._temp_credit_limit = value
    @property
    def temp_limit_valid_time(self):
        return self._temp_limit_valid_time

    @temp_limit_valid_time.setter
    def temp_limit_valid_time(self, value):
        self._temp_limit_valid_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.temp_available_limit:
            if hasattr(self.temp_available_limit, 'to_alipay_dict'):
                params['temp_available_limit'] = self.temp_available_limit.to_alipay_dict()
            else:
                params['temp_available_limit'] = self.temp_available_limit
        if self.temp_credit_limit:
            if hasattr(self.temp_credit_limit, 'to_alipay_dict'):
                params['temp_credit_limit'] = self.temp_credit_limit.to_alipay_dict()
            else:
                params['temp_credit_limit'] = self.temp_credit_limit
        if self.temp_limit_valid_time:
            if hasattr(self.temp_limit_valid_time, 'to_alipay_dict'):
                params['temp_limit_valid_time'] = self.temp_limit_valid_time.to_alipay_dict()
            else:
                params['temp_limit_valid_time'] = self.temp_limit_valid_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HonorTempLimitInfoDTO()
        if 'temp_available_limit' in d:
            o.temp_available_limit = d['temp_available_limit']
        if 'temp_credit_limit' in d:
            o.temp_credit_limit = d['temp_credit_limit']
        if 'temp_limit_valid_time' in d:
            o.temp_limit_valid_time = d['temp_limit_valid_time']
        return o


