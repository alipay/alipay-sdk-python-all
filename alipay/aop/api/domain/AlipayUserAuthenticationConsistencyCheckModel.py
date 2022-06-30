#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAuthenticationConsistencyCheckModel(object):

    def __init__(self):
        self._cert_type = None
        self._encrypt_code = None
        self._user_id = None
        self._user_type = None

    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def encrypt_code(self):
        return self._encrypt_code

    @encrypt_code.setter
    def encrypt_code(self, value):
        self._encrypt_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.encrypt_code:
            if hasattr(self.encrypt_code, 'to_alipay_dict'):
                params['encrypt_code'] = self.encrypt_code.to_alipay_dict()
            else:
                params['encrypt_code'] = self.encrypt_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAuthenticationConsistencyCheckModel()
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'encrypt_code' in d:
            o.encrypt_code = d['encrypt_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


