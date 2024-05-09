#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JhjtestDoc import JhjtestDoc
from alipay.aop.api.domain.JhjTestNew import JhjTestNew


class AlipaySecurityProdJhjtestPredocCancelModel(object):

    def __init__(self):
        self._com_a = None
        self._com_c = None
        self._test_a = None
        self._test_a_openid = None

    @property
    def com_a(self):
        return self._com_a

    @com_a.setter
    def com_a(self, value):
        if isinstance(value, JhjtestDoc):
            self._com_a = value
        else:
            self._com_a = JhjtestDoc.from_alipay_dict(value)
    @property
    def com_c(self):
        return self._com_c

    @com_c.setter
    def com_c(self, value):
        if isinstance(value, JhjTestNew):
            self._com_c = value
        else:
            self._com_c = JhjTestNew.from_alipay_dict(value)
    @property
    def test_a(self):
        return self._test_a

    @test_a.setter
    def test_a(self, value):
        self._test_a = value
    @property
    def test_a_openid(self):
        return self._test_a_openid

    @test_a_openid.setter
    def test_a_openid(self, value):
        self._test_a_openid = value


    def to_alipay_dict(self):
        params = dict()
        if self.com_a:
            if hasattr(self.com_a, 'to_alipay_dict'):
                params['com_a'] = self.com_a.to_alipay_dict()
            else:
                params['com_a'] = self.com_a
        if self.com_c:
            if hasattr(self.com_c, 'to_alipay_dict'):
                params['com_c'] = self.com_c.to_alipay_dict()
            else:
                params['com_c'] = self.com_c
        if self.test_a:
            if hasattr(self.test_a, 'to_alipay_dict'):
                params['test_a'] = self.test_a.to_alipay_dict()
            else:
                params['test_a'] = self.test_a
        if self.test_a_openid:
            if hasattr(self.test_a_openid, 'to_alipay_dict'):
                params['test_a_openid'] = self.test_a_openid.to_alipay_dict()
            else:
                params['test_a_openid'] = self.test_a_openid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdJhjtestPredocCancelModel()
        if 'com_a' in d:
            o.com_a = d['com_a']
        if 'com_c' in d:
            o.com_c = d['com_c']
        if 'test_a' in d:
            o.test_a = d['test_a']
        if 'test_a_openid' in d:
            o.test_a_openid = d['test_a_openid']
        return o


