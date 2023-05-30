#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntSignUrlResult(object):

    def __init__(self):
        self._encrypt_sign_cert_no = None
        self._sign_cert_name = None
        self._sign_cert_no = None
        self._sign_url = None
        self._sign_user_id = None

    @property
    def encrypt_sign_cert_no(self):
        return self._encrypt_sign_cert_no

    @encrypt_sign_cert_no.setter
    def encrypt_sign_cert_no(self, value):
        self._encrypt_sign_cert_no = value
    @property
    def sign_cert_name(self):
        return self._sign_cert_name

    @sign_cert_name.setter
    def sign_cert_name(self, value):
        self._sign_cert_name = value
    @property
    def sign_cert_no(self):
        return self._sign_cert_no

    @sign_cert_no.setter
    def sign_cert_no(self, value):
        self._sign_cert_no = value
    @property
    def sign_url(self):
        return self._sign_url

    @sign_url.setter
    def sign_url(self, value):
        self._sign_url = value
    @property
    def sign_user_id(self):
        return self._sign_user_id

    @sign_user_id.setter
    def sign_user_id(self, value):
        self._sign_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.encrypt_sign_cert_no:
            if hasattr(self.encrypt_sign_cert_no, 'to_alipay_dict'):
                params['encrypt_sign_cert_no'] = self.encrypt_sign_cert_no.to_alipay_dict()
            else:
                params['encrypt_sign_cert_no'] = self.encrypt_sign_cert_no
        if self.sign_cert_name:
            if hasattr(self.sign_cert_name, 'to_alipay_dict'):
                params['sign_cert_name'] = self.sign_cert_name.to_alipay_dict()
            else:
                params['sign_cert_name'] = self.sign_cert_name
        if self.sign_cert_no:
            if hasattr(self.sign_cert_no, 'to_alipay_dict'):
                params['sign_cert_no'] = self.sign_cert_no.to_alipay_dict()
            else:
                params['sign_cert_no'] = self.sign_cert_no
        if self.sign_url:
            if hasattr(self.sign_url, 'to_alipay_dict'):
                params['sign_url'] = self.sign_url.to_alipay_dict()
            else:
                params['sign_url'] = self.sign_url
        if self.sign_user_id:
            if hasattr(self.sign_user_id, 'to_alipay_dict'):
                params['sign_user_id'] = self.sign_user_id.to_alipay_dict()
            else:
                params['sign_user_id'] = self.sign_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntSignUrlResult()
        if 'encrypt_sign_cert_no' in d:
            o.encrypt_sign_cert_no = d['encrypt_sign_cert_no']
        if 'sign_cert_name' in d:
            o.sign_cert_name = d['sign_cert_name']
        if 'sign_cert_no' in d:
            o.sign_cert_no = d['sign_cert_no']
        if 'sign_url' in d:
            o.sign_url = d['sign_url']
        if 'sign_user_id' in d:
            o.sign_user_id = d['sign_user_id']
        return o


