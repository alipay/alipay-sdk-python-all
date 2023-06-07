#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCertificateCertificationPrepareuseModel(object):

    def __init__(self):
        self._code = None
        self._encrypted_data = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def encrypted_data(self):
        return self._encrypted_data

    @encrypted_data.setter
    def encrypted_data(self, value):
        self._encrypted_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.encrypted_data:
            if hasattr(self.encrypted_data, 'to_alipay_dict'):
                params['encrypted_data'] = self.encrypted_data.to_alipay_dict()
            else:
                params['encrypted_data'] = self.encrypted_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCertificateCertificationPrepareuseModel()
        if 'code' in d:
            o.code = d['code']
        if 'encrypted_data' in d:
            o.encrypted_data = d['encrypted_data']
        return o


