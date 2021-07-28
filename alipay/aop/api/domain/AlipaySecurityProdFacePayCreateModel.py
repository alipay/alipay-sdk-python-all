#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdFacePayCreateModel(object):

    def __init__(self):
        self._aaa = None
        self._aaaaaaaaaaaaa = None
        self._bbbbb = None

    @property
    def aaa(self):
        return self._aaa

    @aaa.setter
    def aaa(self, value):
        self._aaa = value
    @property
    def aaaaaaaaaaaaa(self):
        return self._aaaaaaaaaaaaa

    @aaaaaaaaaaaaa.setter
    def aaaaaaaaaaaaa(self, value):
        self._aaaaaaaaaaaaa = value
    @property
    def bbbbb(self):
        return self._bbbbb

    @bbbbb.setter
    def bbbbb(self, value):
        self._bbbbb = value


    def to_alipay_dict(self):
        params = dict()
        if self.aaa:
            if hasattr(self.aaa, 'to_alipay_dict'):
                params['aaa'] = self.aaa.to_alipay_dict()
            else:
                params['aaa'] = self.aaa
        if self.aaaaaaaaaaaaa:
            if hasattr(self.aaaaaaaaaaaaa, 'to_alipay_dict'):
                params['aaaaaaaaaaaaa'] = self.aaaaaaaaaaaaa.to_alipay_dict()
            else:
                params['aaaaaaaaaaaaa'] = self.aaaaaaaaaaaaa
        if self.bbbbb:
            if hasattr(self.bbbbb, 'to_alipay_dict'):
                params['bbbbb'] = self.bbbbb.to_alipay_dict()
            else:
                params['bbbbb'] = self.bbbbb
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdFacePayCreateModel()
        if 'aaa' in d:
            o.aaa = d['aaa']
        if 'aaaaaaaaaaaaa' in d:
            o.aaaaaaaaaaaaa = d['aaaaaaaaaaaaa']
        if 'bbbbb' in d:
            o.bbbbb = d['bbbbb']
        return o


