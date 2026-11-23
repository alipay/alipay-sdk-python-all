#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KLineFailureOpenApiDTO(object):

    def __init__(self):
        self._failure_type = None
        self._reason = None
        self._symbol = None

    @property
    def failure_type(self):
        return self._failure_type

    @failure_type.setter
    def failure_type(self, value):
        self._failure_type = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value


    def to_alipay_dict(self):
        params = dict()
        if self.failure_type:
            if hasattr(self.failure_type, 'to_alipay_dict'):
                params['failure_type'] = self.failure_type.to_alipay_dict()
            else:
                params['failure_type'] = self.failure_type
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.symbol:
            if hasattr(self.symbol, 'to_alipay_dict'):
                params['symbol'] = self.symbol.to_alipay_dict()
            else:
                params['symbol'] = self.symbol
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KLineFailureOpenApiDTO()
        if 'failure_type' in d:
            o.failure_type = d['failure_type']
        if 'reason' in d:
            o.reason = d['reason']
        if 'symbol' in d:
            o.symbol = d['symbol']
        return o


