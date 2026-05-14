#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalAuthenticationTokenVerifyModel(object):

    def __init__(self):
        self._token_data = None
        self._url = None

    @property
    def token_data(self):
        return self._token_data

    @token_data.setter
    def token_data(self, value):
        self._token_data = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.token_data:
            if hasattr(self.token_data, 'to_alipay_dict'):
                params['token_data'] = self.token_data.to_alipay_dict()
            else:
                params['token_data'] = self.token_data
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalAuthenticationTokenVerifyModel()
        if 'token_data' in d:
            o.token_data = d['token_data']
        if 'url' in d:
            o.url = d['url']
        return o


