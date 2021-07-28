#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataPrinterTokenGetModel(object):

    def __init__(self):
        self._client_id = None
        self._grant_type = None
        self._scope = None
        self._secret = None

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value
    @property
    def grant_type(self):
        return self._grant_type

    @grant_type.setter
    def grant_type(self, value):
        self._grant_type = value
    @property
    def scope(self):
        return self._scope

    @scope.setter
    def scope(self, value):
        self._scope = value
    @property
    def secret(self):
        return self._secret

    @secret.setter
    def secret(self, value):
        self._secret = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_id:
            if hasattr(self.client_id, 'to_alipay_dict'):
                params['client_id'] = self.client_id.to_alipay_dict()
            else:
                params['client_id'] = self.client_id
        if self.grant_type:
            if hasattr(self.grant_type, 'to_alipay_dict'):
                params['grant_type'] = self.grant_type.to_alipay_dict()
            else:
                params['grant_type'] = self.grant_type
        if self.scope:
            if hasattr(self.scope, 'to_alipay_dict'):
                params['scope'] = self.scope.to_alipay_dict()
            else:
                params['scope'] = self.scope
        if self.secret:
            if hasattr(self.secret, 'to_alipay_dict'):
                params['secret'] = self.secret.to_alipay_dict()
            else:
                params['secret'] = self.secret
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataPrinterTokenGetModel()
        if 'client_id' in d:
            o.client_id = d['client_id']
        if 'grant_type' in d:
            o.grant_type = d['grant_type']
        if 'scope' in d:
            o.scope = d['scope']
        if 'secret' in d:
            o.secret = d['secret']
        return o


