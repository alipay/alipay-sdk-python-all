#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpRelatedPerformanceQueryModel(object):

    def __init__(self):
        self._company_key = None
        self._product_code = None
        self._ry_cert_no = None
        self._ry_cert_no_sha_256 = None
        self._ry_name = None

    @property
    def company_key(self):
        return self._company_key

    @company_key.setter
    def company_key(self, value):
        self._company_key = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def ry_cert_no(self):
        return self._ry_cert_no

    @ry_cert_no.setter
    def ry_cert_no(self, value):
        self._ry_cert_no = value
    @property
    def ry_cert_no_sha_256(self):
        return self._ry_cert_no_sha_256

    @ry_cert_no_sha_256.setter
    def ry_cert_no_sha_256(self, value):
        self._ry_cert_no_sha_256 = value
    @property
    def ry_name(self):
        return self._ry_name

    @ry_name.setter
    def ry_name(self, value):
        self._ry_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_key:
            if hasattr(self.company_key, 'to_alipay_dict'):
                params['company_key'] = self.company_key.to_alipay_dict()
            else:
                params['company_key'] = self.company_key
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.ry_cert_no:
            if hasattr(self.ry_cert_no, 'to_alipay_dict'):
                params['ry_cert_no'] = self.ry_cert_no.to_alipay_dict()
            else:
                params['ry_cert_no'] = self.ry_cert_no
        if self.ry_cert_no_sha_256:
            if hasattr(self.ry_cert_no_sha_256, 'to_alipay_dict'):
                params['ry_cert_no_sha_256'] = self.ry_cert_no_sha_256.to_alipay_dict()
            else:
                params['ry_cert_no_sha_256'] = self.ry_cert_no_sha_256
        if self.ry_name:
            if hasattr(self.ry_name, 'to_alipay_dict'):
                params['ry_name'] = self.ry_name.to_alipay_dict()
            else:
                params['ry_name'] = self.ry_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpRelatedPerformanceQueryModel()
        if 'company_key' in d:
            o.company_key = d['company_key']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'ry_cert_no' in d:
            o.ry_cert_no = d['ry_cert_no']
        if 'ry_cert_no_sha_256' in d:
            o.ry_cert_no_sha_256 = d['ry_cert_no_sha_256']
        if 'ry_name' in d:
            o.ry_name = d['ry_name']
        return o


