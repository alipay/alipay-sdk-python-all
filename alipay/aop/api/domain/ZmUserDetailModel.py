#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZmUserDetailModel(object):

    def __init__(self):
        self._original_hash = None
        self._original_vector = None
        self._secrect_value = None
        self._secret_key = None

    @property
    def original_hash(self):
        return self._original_hash

    @original_hash.setter
    def original_hash(self, value):
        self._original_hash = value
    @property
    def original_vector(self):
        return self._original_vector

    @original_vector.setter
    def original_vector(self, value):
        self._original_vector = value
    @property
    def secrect_value(self):
        return self._secrect_value

    @secrect_value.setter
    def secrect_value(self, value):
        self._secrect_value = value
    @property
    def secret_key(self):
        return self._secret_key

    @secret_key.setter
    def secret_key(self, value):
        self._secret_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.original_hash:
            if hasattr(self.original_hash, 'to_alipay_dict'):
                params['original_hash'] = self.original_hash.to_alipay_dict()
            else:
                params['original_hash'] = self.original_hash
        if self.original_vector:
            if hasattr(self.original_vector, 'to_alipay_dict'):
                params['original_vector'] = self.original_vector.to_alipay_dict()
            else:
                params['original_vector'] = self.original_vector
        if self.secrect_value:
            if hasattr(self.secrect_value, 'to_alipay_dict'):
                params['secrect_value'] = self.secrect_value.to_alipay_dict()
            else:
                params['secrect_value'] = self.secrect_value
        if self.secret_key:
            if hasattr(self.secret_key, 'to_alipay_dict'):
                params['secret_key'] = self.secret_key.to_alipay_dict()
            else:
                params['secret_key'] = self.secret_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmUserDetailModel()
        if 'original_hash' in d:
            o.original_hash = d['original_hash']
        if 'original_vector' in d:
            o.original_vector = d['original_vector']
        if 'secrect_value' in d:
            o.secrect_value = d['secrect_value']
        if 'secret_key' in d:
            o.secret_key = d['secret_key']
        return o


