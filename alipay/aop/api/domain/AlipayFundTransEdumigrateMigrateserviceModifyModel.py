#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransEdumigrateMigrateserviceModifyModel(object):

    def __init__(self):
        self._handler = None
        self._params = None

    @property
    def handler(self):
        return self._handler

    @handler.setter
    def handler(self, value):
        self._handler = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value


    def to_alipay_dict(self):
        params = dict()
        if self.handler:
            if hasattr(self.handler, 'to_alipay_dict'):
                params['handler'] = self.handler.to_alipay_dict()
            else:
                params['handler'] = self.handler
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransEdumigrateMigrateserviceModifyModel()
        if 'handler' in d:
            o.handler = d['handler']
        if 'params' in d:
            o.params = d['params']
        return o


