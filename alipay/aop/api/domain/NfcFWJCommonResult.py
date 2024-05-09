#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NfcFWJCommonResult(object):

    def __init__(self):
        self._scheme = None
        self._uni_code = None

    @property
    def scheme(self):
        return self._scheme

    @scheme.setter
    def scheme(self, value):
        self._scheme = value
    @property
    def uni_code(self):
        return self._uni_code

    @uni_code.setter
    def uni_code(self, value):
        self._uni_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.scheme:
            if hasattr(self.scheme, 'to_alipay_dict'):
                params['scheme'] = self.scheme.to_alipay_dict()
            else:
                params['scheme'] = self.scheme
        if self.uni_code:
            if hasattr(self.uni_code, 'to_alipay_dict'):
                params['uni_code'] = self.uni_code.to_alipay_dict()
            else:
                params['uni_code'] = self.uni_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NfcFWJCommonResult()
        if 'scheme' in d:
            o.scheme = d['scheme']
        if 'uni_code' in d:
            o.uni_code = d['uni_code']
        return o


