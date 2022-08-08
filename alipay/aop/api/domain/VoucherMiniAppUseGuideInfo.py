#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherMiniAppUseGuideInfo(object):

    def __init__(self):
        self._mini_app_service_codes = None
        self._mini_app_url = None

    @property
    def mini_app_service_codes(self):
        return self._mini_app_service_codes

    @mini_app_service_codes.setter
    def mini_app_service_codes(self, value):
        if isinstance(value, list):
            self._mini_app_service_codes = list()
            for i in value:
                self._mini_app_service_codes.append(i)
    @property
    def mini_app_url(self):
        return self._mini_app_url

    @mini_app_url.setter
    def mini_app_url(self, value):
        self._mini_app_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.mini_app_service_codes:
            if isinstance(self.mini_app_service_codes, list):
                for i in range(0, len(self.mini_app_service_codes)):
                    element = self.mini_app_service_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mini_app_service_codes[i] = element.to_alipay_dict()
            if hasattr(self.mini_app_service_codes, 'to_alipay_dict'):
                params['mini_app_service_codes'] = self.mini_app_service_codes.to_alipay_dict()
            else:
                params['mini_app_service_codes'] = self.mini_app_service_codes
        if self.mini_app_url:
            if hasattr(self.mini_app_url, 'to_alipay_dict'):
                params['mini_app_url'] = self.mini_app_url.to_alipay_dict()
            else:
                params['mini_app_url'] = self.mini_app_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherMiniAppUseGuideInfo()
        if 'mini_app_service_codes' in d:
            o.mini_app_service_codes = d['mini_app_service_codes']
        if 'mini_app_url' in d:
            o.mini_app_url = d['mini_app_url']
        return o


