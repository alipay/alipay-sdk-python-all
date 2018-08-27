#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Principal(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._signer_type = None
        self._user_name = None
        self._verify_type = None

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
    def signer_type(self):
        return self._signer_type

    @signer_type.setter
    def signer_type(self, value):
        self._signer_type = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def verify_type(self):
        return self._verify_type

    @verify_type.setter
    def verify_type(self, value):
        self._verify_type = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.signer_type:
            if hasattr(self.signer_type, 'to_alipay_dict'):
                params['signer_type'] = self.signer_type.to_alipay_dict()
            else:
                params['signer_type'] = self.signer_type
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.verify_type:
            if hasattr(self.verify_type, 'to_alipay_dict'):
                params['verify_type'] = self.verify_type.to_alipay_dict()
            else:
                params['verify_type'] = self.verify_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Principal()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'signer_type' in d:
            o.signer_type = d['signer_type']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'verify_type' in d:
            o.verify_type = d['verify_type']
        return o


