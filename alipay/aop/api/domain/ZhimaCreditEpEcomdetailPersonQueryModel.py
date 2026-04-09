#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpEcomdetailPersonQueryModel(object):

    def __init__(self):
        self._auth_id = None
        self._person_cert_no = None
        self._person_cert_no_md_5 = None
        self._person_cert_no_sha_256 = None
        self._product_code = None

    @property
    def auth_id(self):
        return self._auth_id

    @auth_id.setter
    def auth_id(self, value):
        self._auth_id = value
    @property
    def person_cert_no(self):
        return self._person_cert_no

    @person_cert_no.setter
    def person_cert_no(self, value):
        self._person_cert_no = value
    @property
    def person_cert_no_md_5(self):
        return self._person_cert_no_md_5

    @person_cert_no_md_5.setter
    def person_cert_no_md_5(self, value):
        self._person_cert_no_md_5 = value
    @property
    def person_cert_no_sha_256(self):
        return self._person_cert_no_sha_256

    @person_cert_no_sha_256.setter
    def person_cert_no_sha_256(self, value):
        self._person_cert_no_sha_256 = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_id:
            if hasattr(self.auth_id, 'to_alipay_dict'):
                params['auth_id'] = self.auth_id.to_alipay_dict()
            else:
                params['auth_id'] = self.auth_id
        if self.person_cert_no:
            if hasattr(self.person_cert_no, 'to_alipay_dict'):
                params['person_cert_no'] = self.person_cert_no.to_alipay_dict()
            else:
                params['person_cert_no'] = self.person_cert_no
        if self.person_cert_no_md_5:
            if hasattr(self.person_cert_no_md_5, 'to_alipay_dict'):
                params['person_cert_no_md_5'] = self.person_cert_no_md_5.to_alipay_dict()
            else:
                params['person_cert_no_md_5'] = self.person_cert_no_md_5
        if self.person_cert_no_sha_256:
            if hasattr(self.person_cert_no_sha_256, 'to_alipay_dict'):
                params['person_cert_no_sha_256'] = self.person_cert_no_sha_256.to_alipay_dict()
            else:
                params['person_cert_no_sha_256'] = self.person_cert_no_sha_256
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpEcomdetailPersonQueryModel()
        if 'auth_id' in d:
            o.auth_id = d['auth_id']
        if 'person_cert_no' in d:
            o.person_cert_no = d['person_cert_no']
        if 'person_cert_no_md_5' in d:
            o.person_cert_no_md_5 = d['person_cert_no_md_5']
        if 'person_cert_no_sha_256' in d:
            o.person_cert_no_sha_256 = d['person_cert_no_sha_256']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


