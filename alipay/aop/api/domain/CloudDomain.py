#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CloudDomain(object):

    def __init__(self):
        self._cname = None
        self._force_https = None
        self._has_cert = None
        self._is_custom = None
        self._name = None
        self._ssl_cert = None
        self._ssl_key = None

    @property
    def cname(self):
        return self._cname

    @cname.setter
    def cname(self, value):
        self._cname = value
    @property
    def force_https(self):
        return self._force_https

    @force_https.setter
    def force_https(self, value):
        self._force_https = value
    @property
    def has_cert(self):
        return self._has_cert

    @has_cert.setter
    def has_cert(self, value):
        self._has_cert = value
    @property
    def is_custom(self):
        return self._is_custom

    @is_custom.setter
    def is_custom(self, value):
        self._is_custom = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def ssl_cert(self):
        return self._ssl_cert

    @ssl_cert.setter
    def ssl_cert(self, value):
        self._ssl_cert = value
    @property
    def ssl_key(self):
        return self._ssl_key

    @ssl_key.setter
    def ssl_key(self, value):
        self._ssl_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.cname:
            if hasattr(self.cname, 'to_alipay_dict'):
                params['cname'] = self.cname.to_alipay_dict()
            else:
                params['cname'] = self.cname
        if self.force_https:
            if hasattr(self.force_https, 'to_alipay_dict'):
                params['force_https'] = self.force_https.to_alipay_dict()
            else:
                params['force_https'] = self.force_https
        if self.has_cert:
            if hasattr(self.has_cert, 'to_alipay_dict'):
                params['has_cert'] = self.has_cert.to_alipay_dict()
            else:
                params['has_cert'] = self.has_cert
        if self.is_custom:
            if hasattr(self.is_custom, 'to_alipay_dict'):
                params['is_custom'] = self.is_custom.to_alipay_dict()
            else:
                params['is_custom'] = self.is_custom
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.ssl_cert:
            if hasattr(self.ssl_cert, 'to_alipay_dict'):
                params['ssl_cert'] = self.ssl_cert.to_alipay_dict()
            else:
                params['ssl_cert'] = self.ssl_cert
        if self.ssl_key:
            if hasattr(self.ssl_key, 'to_alipay_dict'):
                params['ssl_key'] = self.ssl_key.to_alipay_dict()
            else:
                params['ssl_key'] = self.ssl_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CloudDomain()
        if 'cname' in d:
            o.cname = d['cname']
        if 'force_https' in d:
            o.force_https = d['force_https']
        if 'has_cert' in d:
            o.has_cert = d['has_cert']
        if 'is_custom' in d:
            o.is_custom = d['is_custom']
        if 'name' in d:
            o.name = d['name']
        if 'ssl_cert' in d:
            o.ssl_cert = d['ssl_cert']
        if 'ssl_key' in d:
            o.ssl_key = d['ssl_key']
        return o


