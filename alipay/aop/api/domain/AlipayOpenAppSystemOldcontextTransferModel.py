#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppSystemOldcontextTransferModel(object):

    def __init__(self):
        self._param_one = None

    @property
    def param_one(self):
        return self._param_one

    @param_one.setter
    def param_one(self, value):
        self._param_one = value


    def to_alipay_dict(self):
        params = dict()
        if self.param_one:
            if hasattr(self.param_one, 'to_alipay_dict'):
                params['param_one'] = self.param_one.to_alipay_dict()
            else:
                params['param_one'] = self.param_one
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppSystemOldcontextTransferModel()
        if 'param_one' in d:
            o.param_one = d['param_one']
        return o


