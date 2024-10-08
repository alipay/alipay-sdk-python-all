#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MdCertificateInfo(object):

    def __init__(self):
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._cert_url = None
        self._gmt_invalid = None
        self._gmt_valid = None

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
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def cert_url(self):
        return self._cert_url

    @cert_url.setter
    def cert_url(self, value):
        self._cert_url = value
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


    def to_alipay_dict(self):
        params = dict()
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
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.cert_url:
            if hasattr(self.cert_url, 'to_alipay_dict'):
                params['cert_url'] = self.cert_url.to_alipay_dict()
            else:
                params['cert_url'] = self.cert_url
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MdCertificateInfo()
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'cert_url' in d:
            o.cert_url = d['cert_url']
        if 'gmt_invalid' in d:
            o.gmt_invalid = d['gmt_invalid']
        if 'gmt_valid' in d:
            o.gmt_valid = d['gmt_valid']
        return o


