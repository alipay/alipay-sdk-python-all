#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AsyncConfigDestination import AsyncConfigDestination
from alipay.aop.api.domain.AsyncConfigDestination import AsyncConfigDestination


class FunctionAsyncConfig(object):

    def __init__(self):
        self._on_failure = None
        self._on_success = None

    @property
    def on_failure(self):
        return self._on_failure

    @on_failure.setter
    def on_failure(self, value):
        if isinstance(value, AsyncConfigDestination):
            self._on_failure = value
        else:
            self._on_failure = AsyncConfigDestination.from_alipay_dict(value)
    @property
    def on_success(self):
        return self._on_success

    @on_success.setter
    def on_success(self, value):
        if isinstance(value, AsyncConfigDestination):
            self._on_success = value
        else:
            self._on_success = AsyncConfigDestination.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.on_failure:
            if hasattr(self.on_failure, 'to_alipay_dict'):
                params['on_failure'] = self.on_failure.to_alipay_dict()
            else:
                params['on_failure'] = self.on_failure
        if self.on_success:
            if hasattr(self.on_success, 'to_alipay_dict'):
                params['on_success'] = self.on_success.to_alipay_dict()
            else:
                params['on_success'] = self.on_success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FunctionAsyncConfig()
        if 'on_failure' in d:
            o.on_failure = d['on_failure']
        if 'on_success' in d:
            o.on_success = d['on_success']
        return o


