#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PublicTestProd import PublicTestProd


class AlipaySecurityProdJhjtestSupportauthtokenModifyModel(object):

    def __init__(self):
        self._aaa = None
        self._com_a = None
        self._is_aasda = None

    @property
    def aaa(self):
        return self._aaa

    @aaa.setter
    def aaa(self, value):
        self._aaa = value
    @property
    def com_a(self):
        return self._com_a

    @com_a.setter
    def com_a(self, value):
        if isinstance(value, PublicTestProd):
            self._com_a = value
        else:
            self._com_a = PublicTestProd.from_alipay_dict(value)
    @property
    def is_aasda(self):
        return self._is_aasda

    @is_aasda.setter
    def is_aasda(self, value):
        self._is_aasda = value


    def to_alipay_dict(self):
        params = dict()
        if self.aaa:
            if hasattr(self.aaa, 'to_alipay_dict'):
                params['aaa'] = self.aaa.to_alipay_dict()
            else:
                params['aaa'] = self.aaa
        if self.com_a:
            if hasattr(self.com_a, 'to_alipay_dict'):
                params['com_a'] = self.com_a.to_alipay_dict()
            else:
                params['com_a'] = self.com_a
        if self.is_aasda:
            if hasattr(self.is_aasda, 'to_alipay_dict'):
                params['is_aasda'] = self.is_aasda.to_alipay_dict()
            else:
                params['is_aasda'] = self.is_aasda
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdJhjtestSupportauthtokenModifyModel()
        if 'aaa' in d:
            o.aaa = d['aaa']
        if 'com_a' in d:
            o.com_a = d['com_a']
        if 'is_aasda' in d:
            o.is_aasda = d['is_aasda']
        return o


