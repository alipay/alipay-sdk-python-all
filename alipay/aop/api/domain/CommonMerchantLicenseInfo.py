#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommonMerchantLicenseInfo(object):

    def __init__(self):
        self._cert_no = None
        self._effective_date = None
        self._license_name = None
        self._license_urls = None
        self._type = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
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
    def license_urls(self):
        return self._license_urls

    @license_urls.setter
    def license_urls(self, value):
        if isinstance(value, list):
            self._license_urls = list()
            for i in value:
                self._license_urls.append(i)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
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
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommonMerchantLicenseInfo()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'effective_date' in d:
            o.effective_date = d['effective_date']
        if 'license_name' in d:
            o.license_name = d['license_name']
        if 'license_urls' in d:
            o.license_urls = d['license_urls']
        if 'type' in d:
            o.type = d['type']
        return o


