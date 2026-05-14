#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdSecdeviceCertifyModel(object):

    def __init__(self):
        self._ifaa_token = None
        self._ifaa_version = None
        self._ifaf_message = None

    @property
    def ifaa_token(self):
        return self._ifaa_token

    @ifaa_token.setter
    def ifaa_token(self, value):
        self._ifaa_token = value
    @property
    def ifaa_version(self):
        return self._ifaa_version

    @ifaa_version.setter
    def ifaa_version(self, value):
        self._ifaa_version = value
    @property
    def ifaf_message(self):
        return self._ifaf_message

    @ifaf_message.setter
    def ifaf_message(self, value):
        self._ifaf_message = value


    def to_alipay_dict(self):
        params = dict()
        if self.ifaa_token:
            if hasattr(self.ifaa_token, 'to_alipay_dict'):
                params['ifaa_token'] = self.ifaa_token.to_alipay_dict()
            else:
                params['ifaa_token'] = self.ifaa_token
        if self.ifaa_version:
            if hasattr(self.ifaa_version, 'to_alipay_dict'):
                params['ifaa_version'] = self.ifaa_version.to_alipay_dict()
            else:
                params['ifaa_version'] = self.ifaa_version
        if self.ifaf_message:
            if hasattr(self.ifaf_message, 'to_alipay_dict'):
                params['ifaf_message'] = self.ifaf_message.to_alipay_dict()
            else:
                params['ifaf_message'] = self.ifaf_message
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdSecdeviceCertifyModel()
        if 'ifaa_token' in d:
            o.ifaa_token = d['ifaa_token']
        if 'ifaa_version' in d:
            o.ifaa_version = d['ifaa_version']
        if 'ifaf_message' in d:
            o.ifaf_message = d['ifaf_message']
        return o


