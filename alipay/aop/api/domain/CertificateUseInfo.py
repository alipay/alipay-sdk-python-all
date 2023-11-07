#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertificateUseInfo(object):

    def __init__(self):
        self._code = None
        self._encrypted_code = None
        self._use_count = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def encrypted_code(self):
        return self._encrypted_code

    @encrypted_code.setter
    def encrypted_code(self, value):
        self._encrypted_code = value
    @property
    def use_count(self):
        return self._use_count

    @use_count.setter
    def use_count(self, value):
        self._use_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.encrypted_code:
            if hasattr(self.encrypted_code, 'to_alipay_dict'):
                params['encrypted_code'] = self.encrypted_code.to_alipay_dict()
            else:
                params['encrypted_code'] = self.encrypted_code
        if self.use_count:
            if hasattr(self.use_count, 'to_alipay_dict'):
                params['use_count'] = self.use_count.to_alipay_dict()
            else:
                params['use_count'] = self.use_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificateUseInfo()
        if 'code' in d:
            o.code = d['code']
        if 'encrypted_code' in d:
            o.encrypted_code = d['encrypted_code']
        if 'use_count' in d:
            o.use_count = d['use_count']
        return o


