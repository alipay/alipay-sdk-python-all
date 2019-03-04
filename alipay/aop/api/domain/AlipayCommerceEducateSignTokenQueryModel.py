#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSignTokenQueryModel(object):

    def __init__(self):
        self._token_key = None

    @property
    def token_key(self):
        return self._token_key

    @token_key.setter
    def token_key(self, value):
        self._token_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.token_key:
            if hasattr(self.token_key, 'to_alipay_dict'):
                params['token_key'] = self.token_key.to_alipay_dict()
            else:
                params['token_key'] = self.token_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSignTokenQueryModel()
        if 'token_key' in d:
            o.token_key = d['token_key']
        return o


