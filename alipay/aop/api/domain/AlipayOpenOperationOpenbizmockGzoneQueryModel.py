#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationOpenbizmockGzoneQueryModel(object):

    def __init__(self):
        self._a = None
        self._a_openid = None

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value
    @property
    def a_openid(self):
        return self._a_openid

    @a_openid.setter
    def a_openid(self, value):
        self._a_openid = value


    def to_alipay_dict(self):
        params = dict()
        if self.a:
            if hasattr(self.a, 'to_alipay_dict'):
                params['a'] = self.a.to_alipay_dict()
            else:
                params['a'] = self.a
        if self.a_openid:
            if hasattr(self.a_openid, 'to_alipay_dict'):
                params['a_openid'] = self.a_openid.to_alipay_dict()
            else:
                params['a_openid'] = self.a_openid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenbizmockGzoneQueryModel()
        if 'a' in d:
            o.a = d['a']
        if 'a_openid' in d:
            o.a_openid = d['a_openid']
        return o


