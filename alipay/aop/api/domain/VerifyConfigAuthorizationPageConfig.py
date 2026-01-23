#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VerifyConfigAuthorizationPageConfig(object):

    def __init__(self):
        self._logo_url = None
        self._main_title = None
        self._verify_interval_limit = None

    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def main_title(self):
        return self._main_title

    @main_title.setter
    def main_title(self, value):
        self._main_title = value
    @property
    def verify_interval_limit(self):
        return self._verify_interval_limit

    @verify_interval_limit.setter
    def verify_interval_limit(self, value):
        self._verify_interval_limit = value


    def to_alipay_dict(self):
        params = dict()
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        if self.main_title:
            if hasattr(self.main_title, 'to_alipay_dict'):
                params['main_title'] = self.main_title.to_alipay_dict()
            else:
                params['main_title'] = self.main_title
        if self.verify_interval_limit:
            if hasattr(self.verify_interval_limit, 'to_alipay_dict'):
                params['verify_interval_limit'] = self.verify_interval_limit.to_alipay_dict()
            else:
                params['verify_interval_limit'] = self.verify_interval_limit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VerifyConfigAuthorizationPageConfig()
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'main_title' in d:
            o.main_title = d['main_title']
        if 'verify_interval_limit' in d:
            o.verify_interval_limit = d['verify_interval_limit']
        return o


