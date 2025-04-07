#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertificateInfoForEntry(object):

    def __init__(self):
        self._business_scope = None
        self._cert_name = None
        self._cert_no = None
        self._cert_pic_url_type = None
        self._cert_pic_urls = None
        self._cert_type = None
        self._gmt_invalid = None
        self._gmt_valid = None
        self._reg_capital = None

    @property
    def business_scope(self):
        return self._business_scope

    @business_scope.setter
    def business_scope(self, value):
        self._business_scope = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_pic_url_type(self):
        return self._cert_pic_url_type

    @cert_pic_url_type.setter
    def cert_pic_url_type(self, value):
        self._cert_pic_url_type = value
    @property
    def cert_pic_urls(self):
        return self._cert_pic_urls

    @cert_pic_urls.setter
    def cert_pic_urls(self, value):
        if isinstance(value, list):
            self._cert_pic_urls = list()
            for i in value:
                self._cert_pic_urls.append(i)
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def gmt_invalid(self):
        return self._gmt_invalid

    @gmt_invalid.setter
    def gmt_invalid(self, value):
        self._gmt_invalid = value
    @property
    def gmt_valid(self):
        return self._gmt_valid

    @gmt_valid.setter
    def gmt_valid(self, value):
        self._gmt_valid = value
    @property
    def reg_capital(self):
        return self._reg_capital

    @reg_capital.setter
    def reg_capital(self, value):
        self._reg_capital = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_scope:
            if hasattr(self.business_scope, 'to_alipay_dict'):
                params['business_scope'] = self.business_scope.to_alipay_dict()
            else:
                params['business_scope'] = self.business_scope
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_pic_url_type:
            if hasattr(self.cert_pic_url_type, 'to_alipay_dict'):
                params['cert_pic_url_type'] = self.cert_pic_url_type.to_alipay_dict()
            else:
                params['cert_pic_url_type'] = self.cert_pic_url_type
        if self.cert_pic_urls:
            if isinstance(self.cert_pic_urls, list):
                for i in range(0, len(self.cert_pic_urls)):
                    element = self.cert_pic_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cert_pic_urls[i] = element.to_alipay_dict()
            if hasattr(self.cert_pic_urls, 'to_alipay_dict'):
                params['cert_pic_urls'] = self.cert_pic_urls.to_alipay_dict()
            else:
                params['cert_pic_urls'] = self.cert_pic_urls
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.gmt_invalid:
            if hasattr(self.gmt_invalid, 'to_alipay_dict'):
                params['gmt_invalid'] = self.gmt_invalid.to_alipay_dict()
            else:
                params['gmt_invalid'] = self.gmt_invalid
        if self.gmt_valid:
            if hasattr(self.gmt_valid, 'to_alipay_dict'):
                params['gmt_valid'] = self.gmt_valid.to_alipay_dict()
            else:
                params['gmt_valid'] = self.gmt_valid
        if self.reg_capital:
            if hasattr(self.reg_capital, 'to_alipay_dict'):
                params['reg_capital'] = self.reg_capital.to_alipay_dict()
            else:
                params['reg_capital'] = self.reg_capital
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificateInfoForEntry()
        if 'business_scope' in d:
            o.business_scope = d['business_scope']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_pic_url_type' in d:
            o.cert_pic_url_type = d['cert_pic_url_type']
        if 'cert_pic_urls' in d:
            o.cert_pic_urls = d['cert_pic_urls']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'gmt_invalid' in d:
            o.gmt_invalid = d['gmt_invalid']
        if 'gmt_valid' in d:
            o.gmt_valid = d['gmt_valid']
        if 'reg_capital' in d:
            o.reg_capital = d['reg_capital']
        return o


