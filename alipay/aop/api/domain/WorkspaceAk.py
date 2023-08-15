#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WorkspaceAk(object):

    def __init__(self):
        self._access_key_id = None
        self._access_key_secret = None

    @property
    def access_key_id(self):
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, value):
        self._access_key_id = value
    @property
    def access_key_secret(self):
        return self._access_key_secret

    @access_key_secret.setter
    def access_key_secret(self, value):
        self._access_key_secret = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_key_id:
            if hasattr(self.access_key_id, 'to_alipay_dict'):
                params['access_key_id'] = self.access_key_id.to_alipay_dict()
            else:
                params['access_key_id'] = self.access_key_id
        if self.access_key_secret:
            if hasattr(self.access_key_secret, 'to_alipay_dict'):
                params['access_key_secret'] = self.access_key_secret.to_alipay_dict()
            else:
                params['access_key_secret'] = self.access_key_secret
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WorkspaceAk()
        if 'access_key_id' in d:
            o.access_key_id = d['access_key_id']
        if 'access_key_secret' in d:
            o.access_key_secret = d['access_key_secret']
        return o


