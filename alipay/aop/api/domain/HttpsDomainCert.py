#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HttpsDomainCert(object):

    def __init__(self):
        self._cert_expiration_time = None
        self._cert_sign_time = None
        self._description = None
        self._domain = None
        self._domain_provider = None
        self._domain_status = None
        self._domain_type = None
        self._id = None
        self._name = None
        self._open = None

    @property
    def cert_expiration_time(self):
        return self._cert_expiration_time

    @cert_expiration_time.setter
    def cert_expiration_time(self, value):
        self._cert_expiration_time = value
    @property
    def cert_sign_time(self):
        return self._cert_sign_time

    @cert_sign_time.setter
    def cert_sign_time(self, value):
        self._cert_sign_time = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        self._domain = value
    @property
    def domain_provider(self):
        return self._domain_provider

    @domain_provider.setter
    def domain_provider(self, value):
        self._domain_provider = value
    @property
    def domain_status(self):
        return self._domain_status

    @domain_status.setter
    def domain_status(self, value):
        self._domain_status = value
    @property
    def domain_type(self):
        return self._domain_type

    @domain_type.setter
    def domain_type(self, value):
        self._domain_type = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open(self):
        return self._open

    @open.setter
    def open(self, value):
        self._open = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_expiration_time:
            if hasattr(self.cert_expiration_time, 'to_alipay_dict'):
                params['cert_expiration_time'] = self.cert_expiration_time.to_alipay_dict()
            else:
                params['cert_expiration_time'] = self.cert_expiration_time
        if self.cert_sign_time:
            if hasattr(self.cert_sign_time, 'to_alipay_dict'):
                params['cert_sign_time'] = self.cert_sign_time.to_alipay_dict()
            else:
                params['cert_sign_time'] = self.cert_sign_time
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.domain:
            if hasattr(self.domain, 'to_alipay_dict'):
                params['domain'] = self.domain.to_alipay_dict()
            else:
                params['domain'] = self.domain
        if self.domain_provider:
            if hasattr(self.domain_provider, 'to_alipay_dict'):
                params['domain_provider'] = self.domain_provider.to_alipay_dict()
            else:
                params['domain_provider'] = self.domain_provider
        if self.domain_status:
            if hasattr(self.domain_status, 'to_alipay_dict'):
                params['domain_status'] = self.domain_status.to_alipay_dict()
            else:
                params['domain_status'] = self.domain_status
        if self.domain_type:
            if hasattr(self.domain_type, 'to_alipay_dict'):
                params['domain_type'] = self.domain_type.to_alipay_dict()
            else:
                params['domain_type'] = self.domain_type
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.open:
            if hasattr(self.open, 'to_alipay_dict'):
                params['open'] = self.open.to_alipay_dict()
            else:
                params['open'] = self.open
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HttpsDomainCert()
        if 'cert_expiration_time' in d:
            o.cert_expiration_time = d['cert_expiration_time']
        if 'cert_sign_time' in d:
            o.cert_sign_time = d['cert_sign_time']
        if 'description' in d:
            o.description = d['description']
        if 'domain' in d:
            o.domain = d['domain']
        if 'domain_provider' in d:
            o.domain_provider = d['domain_provider']
        if 'domain_status' in d:
            o.domain_status = d['domain_status']
        if 'domain_type' in d:
            o.domain_type = d['domain_type']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'open' in d:
            o.open = d['open']
        return o


