#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CodeResult(object):

    def __init__(self):
        self._code = None
        self._code_token = None
        self._code_url = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def code_token(self):
        return self._code_token

    @code_token.setter
    def code_token(self, value):
        self._code_token = value
    @property
    def code_url(self):
        return self._code_url

    @code_url.setter
    def code_url(self, value):
        self._code_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.code_token:
            if hasattr(self.code_token, 'to_alipay_dict'):
                params['code_token'] = self.code_token.to_alipay_dict()
            else:
                params['code_token'] = self.code_token
        if self.code_url:
            if hasattr(self.code_url, 'to_alipay_dict'):
                params['code_url'] = self.code_url.to_alipay_dict()
            else:
                params['code_url'] = self.code_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CodeResult()
        if 'code' in d:
            o.code = d['code']
        if 'code_token' in d:
            o.code_token = d['code_token']
        if 'code_url' in d:
            o.code_url = d['code_url']
        return o


