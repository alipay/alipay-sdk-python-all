#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflinePayMasterKey(object):

    def __init__(self):
        self._key_id = None
        self._public_key = None

    @property
    def key_id(self):
        return self._key_id

    @key_id.setter
    def key_id(self, value):
        self._key_id = value
    @property
    def public_key(self):
        return self._public_key

    @public_key.setter
    def public_key(self, value):
        self._public_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.key_id:
            if hasattr(self.key_id, 'to_alipay_dict'):
                params['key_id'] = self.key_id.to_alipay_dict()
            else:
                params['key_id'] = self.key_id
        if self.public_key:
            if hasattr(self.public_key, 'to_alipay_dict'):
                params['public_key'] = self.public_key.to_alipay_dict()
            else:
                params['public_key'] = self.public_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflinePayMasterKey()
        if 'key_id' in d:
            o.key_id = d['key_id']
        if 'public_key' in d:
            o.public_key = d['public_key']
        return o


