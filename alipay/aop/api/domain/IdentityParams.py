#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IdentityParams(object):

    def __init__(self):
        self._cert_no = None
        self._identity_hash = None
        self._sign_user_id = None
        self._user_name = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def identity_hash(self):
        return self._identity_hash

    @identity_hash.setter
    def identity_hash(self, value):
        self._identity_hash = value
    @property
    def sign_user_id(self):
        return self._sign_user_id

    @sign_user_id.setter
    def sign_user_id(self, value):
        self._sign_user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.identity_hash:
            if hasattr(self.identity_hash, 'to_alipay_dict'):
                params['identity_hash'] = self.identity_hash.to_alipay_dict()
            else:
                params['identity_hash'] = self.identity_hash
        if self.sign_user_id:
            if hasattr(self.sign_user_id, 'to_alipay_dict'):
                params['sign_user_id'] = self.sign_user_id.to_alipay_dict()
            else:
                params['sign_user_id'] = self.sign_user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IdentityParams()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'identity_hash' in d:
            o.identity_hash = d['identity_hash']
        if 'sign_user_id' in d:
            o.sign_user_id = d['sign_user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


