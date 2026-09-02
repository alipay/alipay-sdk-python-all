#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IsvAuthResult(object):

    def __init__(self):
        self._auth_status = None
        self._expires_in = None
        self._re_expires_in = None

    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value
    @property
    def expires_in(self):
        return self._expires_in

    @expires_in.setter
    def expires_in(self, value):
        self._expires_in = value
    @property
    def re_expires_in(self):
        return self._re_expires_in

    @re_expires_in.setter
    def re_expires_in(self, value):
        self._re_expires_in = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_status:
            if hasattr(self.auth_status, 'to_alipay_dict'):
                params['auth_status'] = self.auth_status.to_alipay_dict()
            else:
                params['auth_status'] = self.auth_status
        if self.expires_in:
            if hasattr(self.expires_in, 'to_alipay_dict'):
                params['expires_in'] = self.expires_in.to_alipay_dict()
            else:
                params['expires_in'] = self.expires_in
        if self.re_expires_in:
            if hasattr(self.re_expires_in, 'to_alipay_dict'):
                params['re_expires_in'] = self.re_expires_in.to_alipay_dict()
            else:
                params['re_expires_in'] = self.re_expires_in
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IsvAuthResult()
        if 'auth_status' in d:
            o.auth_status = d['auth_status']
        if 'expires_in' in d:
            o.expires_in = d['expires_in']
        if 're_expires_in' in d:
            o.re_expires_in = d['re_expires_in']
        return o


