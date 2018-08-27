#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAuthTokenAppModel(object):

    def __init__(self):
        self._code = None
        self._grant_type = None
        self._refresh_token = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def grant_type(self):
        return self._grant_type

    @grant_type.setter
    def grant_type(self, value):
        self._grant_type = value
    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self._refresh_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.grant_type:
            if hasattr(self.grant_type, 'to_alipay_dict'):
                params['grant_type'] = self.grant_type.to_alipay_dict()
            else:
                params['grant_type'] = self.grant_type
        if self.refresh_token:
            if hasattr(self.refresh_token, 'to_alipay_dict'):
                params['refresh_token'] = self.refresh_token.to_alipay_dict()
            else:
                params['refresh_token'] = self.refresh_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAuthTokenAppModel()
        if 'code' in d:
            o.code = d['code']
        if 'grant_type' in d:
            o.grant_type = d['grant_type']
        if 'refresh_token' in d:
            o.refresh_token = d['refresh_token']
        return o


