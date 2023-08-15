#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Config(object):

    def __init__(self):
        self._max_concurrency = None
        self._max_idle_timeout = None
        self._max_req_timeout = None
        self._max_retry_time = None

    @property
    def max_concurrency(self):
        return self._max_concurrency

    @max_concurrency.setter
    def max_concurrency(self, value):
        self._max_concurrency = value
    @property
    def max_idle_timeout(self):
        return self._max_idle_timeout

    @max_idle_timeout.setter
    def max_idle_timeout(self, value):
        self._max_idle_timeout = value
    @property
    def max_req_timeout(self):
        return self._max_req_timeout

    @max_req_timeout.setter
    def max_req_timeout(self, value):
        self._max_req_timeout = value
    @property
    def max_retry_time(self):
        return self._max_retry_time

    @max_retry_time.setter
    def max_retry_time(self, value):
        self._max_retry_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_concurrency:
            if hasattr(self.max_concurrency, 'to_alipay_dict'):
                params['max_concurrency'] = self.max_concurrency.to_alipay_dict()
            else:
                params['max_concurrency'] = self.max_concurrency
        if self.max_idle_timeout:
            if hasattr(self.max_idle_timeout, 'to_alipay_dict'):
                params['max_idle_timeout'] = self.max_idle_timeout.to_alipay_dict()
            else:
                params['max_idle_timeout'] = self.max_idle_timeout
        if self.max_req_timeout:
            if hasattr(self.max_req_timeout, 'to_alipay_dict'):
                params['max_req_timeout'] = self.max_req_timeout.to_alipay_dict()
            else:
                params['max_req_timeout'] = self.max_req_timeout
        if self.max_retry_time:
            if hasattr(self.max_retry_time, 'to_alipay_dict'):
                params['max_retry_time'] = self.max_retry_time.to_alipay_dict()
            else:
                params['max_retry_time'] = self.max_retry_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Config()
        if 'max_concurrency' in d:
            o.max_concurrency = d['max_concurrency']
        if 'max_idle_timeout' in d:
            o.max_idle_timeout = d['max_idle_timeout']
        if 'max_req_timeout' in d:
            o.max_req_timeout = d['max_req_timeout']
        if 'max_retry_time' in d:
            o.max_retry_time = d['max_retry_time']
        return o


