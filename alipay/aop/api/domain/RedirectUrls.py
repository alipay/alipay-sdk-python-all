#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RedirectUrls(object):

    def __init__(self):
        self._redirect_url = None
        self._verify_type = None

    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value
    @property
    def verify_type(self):
        return self._verify_type

    @verify_type.setter
    def verify_type(self, value):
        self._verify_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        if self.verify_type:
            if hasattr(self.verify_type, 'to_alipay_dict'):
                params['verify_type'] = self.verify_type.to_alipay_dict()
            else:
                params['verify_type'] = self.verify_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RedirectUrls()
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        if 'verify_type' in d:
            o.verify_type = d['verify_type']
        return o


