#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdAntlegalchainNotaryQueryModel(object):

    def __init__(self):
        self._app_code = None
        self._business_unique_id = None
        self._token_key = None

    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def business_unique_id(self):
        return self._business_unique_id

    @business_unique_id.setter
    def business_unique_id(self, value):
        self._business_unique_id = value
    @property
    def token_key(self):
        return self._token_key

    @token_key.setter
    def token_key(self, value):
        self._token_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.business_unique_id:
            if hasattr(self.business_unique_id, 'to_alipay_dict'):
                params['business_unique_id'] = self.business_unique_id.to_alipay_dict()
            else:
                params['business_unique_id'] = self.business_unique_id
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
        o = AlipayBossProdAntlegalchainNotaryQueryModel()
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'business_unique_id' in d:
            o.business_unique_id = d['business_unique_id']
        if 'token_key' in d:
            o.token_key = d['token_key']
        return o


