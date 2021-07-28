#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiProvisioningBundle(object):

    def __init__(self):
        self._data = None
        self._ephemeral_public_key = None
        self._public_key_hash = None
        self._version = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def ephemeral_public_key(self):
        return self._ephemeral_public_key

    @ephemeral_public_key.setter
    def ephemeral_public_key(self, value):
        self._ephemeral_public_key = value
    @property
    def public_key_hash(self):
        return self._public_key_hash

    @public_key_hash.setter
    def public_key_hash(self, value):
        self._public_key_hash = value
    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.ephemeral_public_key:
            if hasattr(self.ephemeral_public_key, 'to_alipay_dict'):
                params['ephemeral_public_key'] = self.ephemeral_public_key.to_alipay_dict()
            else:
                params['ephemeral_public_key'] = self.ephemeral_public_key
        if self.public_key_hash:
            if hasattr(self.public_key_hash, 'to_alipay_dict'):
                params['public_key_hash'] = self.public_key_hash.to_alipay_dict()
            else:
                params['public_key_hash'] = self.public_key_hash
        if self.version:
            if hasattr(self.version, 'to_alipay_dict'):
                params['version'] = self.version.to_alipay_dict()
            else:
                params['version'] = self.version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiProvisioningBundle()
        if 'data' in d:
            o.data = d['data']
        if 'ephemeral_public_key' in d:
            o.ephemeral_public_key = d['ephemeral_public_key']
        if 'public_key_hash' in d:
            o.public_key_hash = d['public_key_hash']
        if 'version' in d:
            o.version = d['version']
        return o


