#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenBpaasServiceBindModel(object):

    def __init__(self):
        self._bpaas_app_id = None
        self._bpaas_app_version = None
        self._service_code = None
        self._service_version = None

    @property
    def bpaas_app_id(self):
        return self._bpaas_app_id

    @bpaas_app_id.setter
    def bpaas_app_id(self, value):
        self._bpaas_app_id = value
    @property
    def bpaas_app_version(self):
        return self._bpaas_app_version

    @bpaas_app_version.setter
    def bpaas_app_version(self, value):
        self._bpaas_app_version = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_version(self):
        return self._service_version

    @service_version.setter
    def service_version(self, value):
        self._service_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.bpaas_app_id:
            if hasattr(self.bpaas_app_id, 'to_alipay_dict'):
                params['bpaas_app_id'] = self.bpaas_app_id.to_alipay_dict()
            else:
                params['bpaas_app_id'] = self.bpaas_app_id
        if self.bpaas_app_version:
            if hasattr(self.bpaas_app_version, 'to_alipay_dict'):
                params['bpaas_app_version'] = self.bpaas_app_version.to_alipay_dict()
            else:
                params['bpaas_app_version'] = self.bpaas_app_version
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_version:
            if hasattr(self.service_version, 'to_alipay_dict'):
                params['service_version'] = self.service_version.to_alipay_dict()
            else:
                params['service_version'] = self.service_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenBpaasServiceBindModel()
        if 'bpaas_app_id' in d:
            o.bpaas_app_id = d['bpaas_app_id']
        if 'bpaas_app_version' in d:
            o.bpaas_app_version = d['bpaas_app_version']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_version' in d:
            o.service_version = d['service_version']
        return o


