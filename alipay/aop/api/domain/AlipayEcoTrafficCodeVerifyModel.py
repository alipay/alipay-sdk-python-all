#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoTrafficCodeVerifyModel(object):

    def __init__(self):
        self._cert_service_type = None
        self._cert_type = None
        self._offline_cert = None
        self._parse_mode = None
        self._user_id = None

    @property
    def cert_service_type(self):
        return self._cert_service_type

    @cert_service_type.setter
    def cert_service_type(self, value):
        self._cert_service_type = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def offline_cert(self):
        return self._offline_cert

    @offline_cert.setter
    def offline_cert(self, value):
        self._offline_cert = value
    @property
    def parse_mode(self):
        return self._parse_mode

    @parse_mode.setter
    def parse_mode(self, value):
        self._parse_mode = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_service_type:
            if hasattr(self.cert_service_type, 'to_alipay_dict'):
                params['cert_service_type'] = self.cert_service_type.to_alipay_dict()
            else:
                params['cert_service_type'] = self.cert_service_type
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.offline_cert:
            if hasattr(self.offline_cert, 'to_alipay_dict'):
                params['offline_cert'] = self.offline_cert.to_alipay_dict()
            else:
                params['offline_cert'] = self.offline_cert
        if self.parse_mode:
            if hasattr(self.parse_mode, 'to_alipay_dict'):
                params['parse_mode'] = self.parse_mode.to_alipay_dict()
            else:
                params['parse_mode'] = self.parse_mode
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoTrafficCodeVerifyModel()
        if 'cert_service_type' in d:
            o.cert_service_type = d['cert_service_type']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'offline_cert' in d:
            o.offline_cert = d['offline_cert']
        if 'parse_mode' in d:
            o.parse_mode = d['parse_mode']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


