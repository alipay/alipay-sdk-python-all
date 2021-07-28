#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoEprintTokenGetModel(object):

    def __init__(self):
        self._cache_first = None
        self._client_id = None
        self._client_secret = None

    @property
    def cache_first(self):
        return self._cache_first

    @cache_first.setter
    def cache_first(self, value):
        self._cache_first = value
    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value
    @property
    def client_secret(self):
        return self._client_secret

    @client_secret.setter
    def client_secret(self, value):
        self._client_secret = value


    def to_alipay_dict(self):
        params = dict()
        if self.cache_first:
            if hasattr(self.cache_first, 'to_alipay_dict'):
                params['cache_first'] = self.cache_first.to_alipay_dict()
            else:
                params['cache_first'] = self.cache_first
        if self.client_id:
            if hasattr(self.client_id, 'to_alipay_dict'):
                params['client_id'] = self.client_id.to_alipay_dict()
            else:
                params['client_id'] = self.client_id
        if self.client_secret:
            if hasattr(self.client_secret, 'to_alipay_dict'):
                params['client_secret'] = self.client_secret.to_alipay_dict()
            else:
                params['client_secret'] = self.client_secret
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEprintTokenGetModel()
        if 'cache_first' in d:
            o.cache_first = d['cache_first']
        if 'client_id' in d:
            o.client_id = d['client_id']
        if 'client_secret' in d:
            o.client_secret = d['client_secret']
        return o


