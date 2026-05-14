#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentUserIdentityInfo(object):

    def __init__(self):
        self._content = None
        self._secure_key = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def secure_key(self):
        return self._secure_key

    @secure_key.setter
    def secure_key(self, value):
        self._secure_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.secure_key:
            if hasattr(self.secure_key, 'to_alipay_dict'):
                params['secure_key'] = self.secure_key.to_alipay_dict()
            else:
                params['secure_key'] = self.secure_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentUserIdentityInfo()
        if 'content' in d:
            o.content = d['content']
        if 'secure_key' in d:
            o.secure_key = d['secure_key']
        return o


