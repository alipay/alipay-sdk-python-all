#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdFingerprintVerifyInitializeModel(object):

    def __init__(self):
        self._ifaa_version = None
        self._sec_data = None
        self._token = None

    @property
    def ifaa_version(self):
        return self._ifaa_version

    @ifaa_version.setter
    def ifaa_version(self, value):
        self._ifaa_version = value
    @property
    def sec_data(self):
        return self._sec_data

    @sec_data.setter
    def sec_data(self, value):
        self._sec_data = value
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value


    def to_alipay_dict(self):
        params = dict()
        if self.ifaa_version:
            if hasattr(self.ifaa_version, 'to_alipay_dict'):
                params['ifaa_version'] = self.ifaa_version.to_alipay_dict()
            else:
                params['ifaa_version'] = self.ifaa_version
        if self.sec_data:
            if hasattr(self.sec_data, 'to_alipay_dict'):
                params['sec_data'] = self.sec_data.to_alipay_dict()
            else:
                params['sec_data'] = self.sec_data
        if self.token:
            if hasattr(self.token, 'to_alipay_dict'):
                params['token'] = self.token.to_alipay_dict()
            else:
                params['token'] = self.token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdFingerprintVerifyInitializeModel()
        if 'ifaa_version' in d:
            o.ifaa_version = d['ifaa_version']
        if 'sec_data' in d:
            o.sec_data = d['sec_data']
        if 'token' in d:
            o.token = d['token']
        return o


