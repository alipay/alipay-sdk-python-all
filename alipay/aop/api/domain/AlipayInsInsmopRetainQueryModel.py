#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsInsmopRetainQueryModel(object):

    def __init__(self):
        self._access_token = None
        self._ins_code = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def ins_code(self):
        return self._ins_code

    @ins_code.setter
    def ins_code(self, value):
        self._ins_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_token:
            if hasattr(self.access_token, 'to_alipay_dict'):
                params['access_token'] = self.access_token.to_alipay_dict()
            else:
                params['access_token'] = self.access_token
        if self.ins_code:
            if hasattr(self.ins_code, 'to_alipay_dict'):
                params['ins_code'] = self.ins_code.to_alipay_dict()
            else:
                params['ins_code'] = self.ins_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsInsmopRetainQueryModel()
        if 'access_token' in d:
            o.access_token = d['access_token']
        if 'ins_code' in d:
            o.ins_code = d['ins_code']
        return o


