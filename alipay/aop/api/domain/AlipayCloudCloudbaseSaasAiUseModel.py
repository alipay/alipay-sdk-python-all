#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseSaasAiUseModel(object):

    def __init__(self):
        self._service_code = None
        self._uri = None

    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def uri(self):
        return self._uri

    @uri.setter
    def uri(self, value):
        self._uri = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.uri:
            if hasattr(self.uri, 'to_alipay_dict'):
                params['uri'] = self.uri.to_alipay_dict()
            else:
                params['uri'] = self.uri
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseSaasAiUseModel()
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'uri' in d:
            o.uri = d['uri']
        return o


