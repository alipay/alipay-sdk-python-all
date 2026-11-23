#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MlmParamTest import MlmParamTest


class MlmParamTestDemo(object):

    def __init__(self):
        self._param_a = None
        self._param_a_openid = None
        self._param_complex = None

    @property
    def param_a(self):
        return self._param_a

    @param_a.setter
    def param_a(self, value):
        self._param_a = value
    @property
    def param_a_openid(self):
        return self._param_a_openid

    @param_a_openid.setter
    def param_a_openid(self, value):
        self._param_a_openid = value
    @property
    def param_complex(self):
        return self._param_complex

    @param_complex.setter
    def param_complex(self, value):
        if isinstance(value, MlmParamTest):
            self._param_complex = value
        else:
            self._param_complex = MlmParamTest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.param_a:
            if hasattr(self.param_a, 'to_alipay_dict'):
                params['param_a'] = self.param_a.to_alipay_dict()
            else:
                params['param_a'] = self.param_a
        if self.param_a_openid:
            if hasattr(self.param_a_openid, 'to_alipay_dict'):
                params['param_a_openid'] = self.param_a_openid.to_alipay_dict()
            else:
                params['param_a_openid'] = self.param_a_openid
        if self.param_complex:
            if hasattr(self.param_complex, 'to_alipay_dict'):
                params['param_complex'] = self.param_complex.to_alipay_dict()
            else:
                params['param_complex'] = self.param_complex
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MlmParamTestDemo()
        if 'param_a' in d:
            o.param_a = d['param_a']
        if 'param_a_openid' in d:
            o.param_a_openid = d['param_a_openid']
        if 'param_complex' in d:
            o.param_complex = d['param_complex']
        return o


