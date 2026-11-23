#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class McpAuthorization(object):

    def __init__(self):
        self._api_key_authorization = None

    @property
    def api_key_authorization(self):
        return self._api_key_authorization

    @api_key_authorization.setter
    def api_key_authorization(self, value):
        self._api_key_authorization = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_key_authorization:
            if hasattr(self.api_key_authorization, 'to_alipay_dict'):
                params['api_key_authorization'] = self.api_key_authorization.to_alipay_dict()
            else:
                params['api_key_authorization'] = self.api_key_authorization
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = McpAuthorization()
        if 'api_key_authorization' in d:
            o.api_key_authorization = d['api_key_authorization']
        return o


