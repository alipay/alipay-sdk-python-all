#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerJobworthAuthenticationpluginQueryModel(object):

    def __init__(self):
        self._sign_str = None

    @property
    def sign_str(self):
        return self._sign_str

    @sign_str.setter
    def sign_str(self, value):
        self._sign_str = value


    def to_alipay_dict(self):
        params = dict()
        if self.sign_str:
            if hasattr(self.sign_str, 'to_alipay_dict'):
                params['sign_str'] = self.sign_str.to_alipay_dict()
            else:
                params['sign_str'] = self.sign_str
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerJobworthAuthenticationpluginQueryModel()
        if 'sign_str' in d:
            o.sign_str = d['sign_str']
        return o


