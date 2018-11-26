#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdDeviceinfoQueryModel(object):

    def __init__(self):
        self._terminal_type = None
        self._token_id = None

    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value
    @property
    def token_id(self):
        return self._token_id

    @token_id.setter
    def token_id(self, value):
        self._token_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.terminal_type:
            if hasattr(self.terminal_type, 'to_alipay_dict'):
                params['terminal_type'] = self.terminal_type.to_alipay_dict()
            else:
                params['terminal_type'] = self.terminal_type
        if self.token_id:
            if hasattr(self.token_id, 'to_alipay_dict'):
                params['token_id'] = self.token_id.to_alipay_dict()
            else:
                params['token_id'] = self.token_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdDeviceinfoQueryModel()
        if 'terminal_type' in d:
            o.terminal_type = d['terminal_type']
        if 'token_id' in d:
            o.token_id = d['token_id']
        return o


