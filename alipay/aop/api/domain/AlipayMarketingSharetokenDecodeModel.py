#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingSharetokenDecodeModel(object):

    def __init__(self):
        self._code_type = None
        self._ext_data = None
        self._token = None

    @property
    def code_type(self):
        return self._code_type

    @code_type.setter
    def code_type(self, value):
        self._code_type = value
    @property
    def ext_data(self):
        return self._ext_data

    @ext_data.setter
    def ext_data(self, value):
        self._ext_data = value
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value


    def to_alipay_dict(self):
        params = dict()
        if self.code_type:
            if hasattr(self.code_type, 'to_alipay_dict'):
                params['code_type'] = self.code_type.to_alipay_dict()
            else:
                params['code_type'] = self.code_type
        if self.ext_data:
            if hasattr(self.ext_data, 'to_alipay_dict'):
                params['ext_data'] = self.ext_data.to_alipay_dict()
            else:
                params['ext_data'] = self.ext_data
        if self.token:
            if hasattr(self.token, 'to_alipay_dict'):
                params['token'] = self.token.to_alipay_dict()
            else:
                params['token'] = self.token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingSharetokenDecodeModel()
        if 'code_type' in d:
            o.code_type = d['code_type']
        if 'ext_data' in d:
            o.ext_data = d['ext_data']
        if 'token' in d:
            o.token = d['token']
        return o


