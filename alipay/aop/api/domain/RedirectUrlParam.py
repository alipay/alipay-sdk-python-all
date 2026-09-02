#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RedirectUrlParam(object):

    def __init__(self):
        self._client = None
        self._redirect_url = None

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        self._client = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.client:
            if hasattr(self.client, 'to_alipay_dict'):
                params['client'] = self.client.to_alipay_dict()
            else:
                params['client'] = self.client
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RedirectUrlParam()
        if 'client' in d:
            o.client = d['client']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        return o


