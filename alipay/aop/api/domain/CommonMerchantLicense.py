#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommonMerchantLicense(object):

    def __init__(self):
        self._code = None
        self._effective_date = None
        self._license_name = None
        self._license_type = None
        self._license_urls = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def effective_date(self):
        return self._effective_date

    @effective_date.setter
    def effective_date(self, value):
        self._effective_date = value
    @property
    def license_name(self):
        return self._license_name

    @license_name.setter
    def license_name(self, value):
        self._license_name = value
    @property
    def license_type(self):
        return self._license_type

    @license_type.setter
    def license_type(self, value):
        self._license_type = value
    @property
    def license_urls(self):
        return self._license_urls

    @license_urls.setter
    def license_urls(self, value):
        if isinstance(value, list):
            self._license_urls = list()
            for i in value:
                self._license_urls.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.effective_date:
            if hasattr(self.effective_date, 'to_alipay_dict'):
                params['effective_date'] = self.effective_date.to_alipay_dict()
            else:
                params['effective_date'] = self.effective_date
        if self.license_name:
            if hasattr(self.license_name, 'to_alipay_dict'):
                params['license_name'] = self.license_name.to_alipay_dict()
            else:
                params['license_name'] = self.license_name
        if self.license_type:
            if hasattr(self.license_type, 'to_alipay_dict'):
                params['license_type'] = self.license_type.to_alipay_dict()
            else:
                params['license_type'] = self.license_type
        if self.license_urls:
            if isinstance(self.license_urls, list):
                for i in range(0, len(self.license_urls)):
                    element = self.license_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.license_urls[i] = element.to_alipay_dict()
            if hasattr(self.license_urls, 'to_alipay_dict'):
                params['license_urls'] = self.license_urls.to_alipay_dict()
            else:
                params['license_urls'] = self.license_urls
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommonMerchantLicense()
        if 'code' in d:
            o.code = d['code']
        if 'effective_date' in d:
            o.effective_date = d['effective_date']
        if 'license_name' in d:
            o.license_name = d['license_name']
        if 'license_type' in d:
            o.license_type = d['license_type']
        if 'license_urls' in d:
            o.license_urls = d['license_urls']
        return o


