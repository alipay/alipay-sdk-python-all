#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdIfaaDevicepubkeyQueryModel(object):

    def __init__(self):
        self._ecdh_publickey = None
        self._max_id = None
        self._security_device_id = None
        self._security_schema = None

    @property
    def ecdh_publickey(self):
        return self._ecdh_publickey

    @ecdh_publickey.setter
    def ecdh_publickey(self, value):
        self._ecdh_publickey = value
    @property
    def max_id(self):
        return self._max_id

    @max_id.setter
    def max_id(self, value):
        self._max_id = value
    @property
    def security_device_id(self):
        return self._security_device_id

    @security_device_id.setter
    def security_device_id(self, value):
        self._security_device_id = value
    @property
    def security_schema(self):
        return self._security_schema

    @security_schema.setter
    def security_schema(self, value):
        self._security_schema = value


    def to_alipay_dict(self):
        params = dict()
        if self.ecdh_publickey:
            if hasattr(self.ecdh_publickey, 'to_alipay_dict'):
                params['ecdh_publickey'] = self.ecdh_publickey.to_alipay_dict()
            else:
                params['ecdh_publickey'] = self.ecdh_publickey
        if self.max_id:
            if hasattr(self.max_id, 'to_alipay_dict'):
                params['max_id'] = self.max_id.to_alipay_dict()
            else:
                params['max_id'] = self.max_id
        if self.security_device_id:
            if hasattr(self.security_device_id, 'to_alipay_dict'):
                params['security_device_id'] = self.security_device_id.to_alipay_dict()
            else:
                params['security_device_id'] = self.security_device_id
        if self.security_schema:
            if hasattr(self.security_schema, 'to_alipay_dict'):
                params['security_schema'] = self.security_schema.to_alipay_dict()
            else:
                params['security_schema'] = self.security_schema
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdIfaaDevicepubkeyQueryModel()
        if 'ecdh_publickey' in d:
            o.ecdh_publickey = d['ecdh_publickey']
        if 'max_id' in d:
            o.max_id = d['max_id']
        if 'security_device_id' in d:
            o.security_device_id = d['security_device_id']
        if 'security_schema' in d:
            o.security_schema = d['security_schema']
        return o


