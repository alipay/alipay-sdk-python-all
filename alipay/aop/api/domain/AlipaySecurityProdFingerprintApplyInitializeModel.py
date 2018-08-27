#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdFingerprintApplyInitializeModel(object):

    def __init__(self):
        self._auth_type = None
        self._ifaa_version = None
        self._sec_data = None

    @property
    def auth_type(self):
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        self._auth_type = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.auth_type:
            if hasattr(self.auth_type, 'to_alipay_dict'):
                params['auth_type'] = self.auth_type.to_alipay_dict()
            else:
                params['auth_type'] = self.auth_type
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdFingerprintApplyInitializeModel()
        if 'auth_type' in d:
            o.auth_type = d['auth_type']
        if 'ifaa_version' in d:
            o.ifaa_version = d['ifaa_version']
        if 'sec_data' in d:
            o.sec_data = d['sec_data']
        return o


