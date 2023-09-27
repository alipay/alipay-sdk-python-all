#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertifyPlatformInfo(object):

    def __init__(self):
        self._certify_platform_name = None
        self._certify_platform_url = None

    @property
    def certify_platform_name(self):
        return self._certify_platform_name

    @certify_platform_name.setter
    def certify_platform_name(self, value):
        self._certify_platform_name = value
    @property
    def certify_platform_url(self):
        return self._certify_platform_url

    @certify_platform_url.setter
    def certify_platform_url(self, value):
        self._certify_platform_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.certify_platform_name:
            if hasattr(self.certify_platform_name, 'to_alipay_dict'):
                params['certify_platform_name'] = self.certify_platform_name.to_alipay_dict()
            else:
                params['certify_platform_name'] = self.certify_platform_name
        if self.certify_platform_url:
            if hasattr(self.certify_platform_url, 'to_alipay_dict'):
                params['certify_platform_url'] = self.certify_platform_url.to_alipay_dict()
            else:
                params['certify_platform_url'] = self.certify_platform_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertifyPlatformInfo()
        if 'certify_platform_name' in d:
            o.certify_platform_name = d['certify_platform_name']
        if 'certify_platform_url' in d:
            o.certify_platform_url = d['certify_platform_url']
        return o


