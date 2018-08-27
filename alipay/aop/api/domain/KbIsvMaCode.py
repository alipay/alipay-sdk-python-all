#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbIsvMaCode(object):

    def __init__(self):
        self._code = None
        self._num = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.num:
            if hasattr(self.num, 'to_alipay_dict'):
                params['num'] = self.num.to_alipay_dict()
            else:
                params['num'] = self.num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbIsvMaCode()
        if 'code' in d:
            o.code = d['code']
        if 'num' in d:
            o.num = d['num']
        return o


