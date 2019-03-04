#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPeUserAuthApplyModel(object):

    def __init__(self):
        self._product_code = None
        self._redirect_uri = None
        self._scope = None
        self._state = None

    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def redirect_uri(self):
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, value):
        self._redirect_uri = value
    @property
    def scope(self):
        return self._scope

    @scope.setter
    def scope(self, value):
        self._scope = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value


    def to_alipay_dict(self):
        params = dict()
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.redirect_uri:
            if hasattr(self.redirect_uri, 'to_alipay_dict'):
                params['redirect_uri'] = self.redirect_uri.to_alipay_dict()
            else:
                params['redirect_uri'] = self.redirect_uri
        if self.scope:
            if hasattr(self.scope, 'to_alipay_dict'):
                params['scope'] = self.scope.to_alipay_dict()
            else:
                params['scope'] = self.scope
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeUserAuthApplyModel()
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'redirect_uri' in d:
            o.redirect_uri = d['redirect_uri']
        if 'scope' in d:
            o.scope = d['scope']
        if 'state' in d:
            o.state = d['state']
        return o


