#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceTitleDynamicGetModel(object):

    def __init__(self):
        self._bar_code = None

    @property
    def bar_code(self):
        return self._bar_code

    @bar_code.setter
    def bar_code(self, value):
        self._bar_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.bar_code:
            if hasattr(self.bar_code, 'to_alipay_dict'):
                params['bar_code'] = self.bar_code.to_alipay_dict()
            else:
                params['bar_code'] = self.bar_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceTitleDynamicGetModel()
        if 'bar_code' in d:
            o.bar_code = d['bar_code']
        return o


