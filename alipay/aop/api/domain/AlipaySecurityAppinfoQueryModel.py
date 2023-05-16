#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityAppinfoQueryModel(object):

    def __init__(self):
        self._aaa = None

    @property
    def aaa(self):
        return self._aaa

    @aaa.setter
    def aaa(self, value):
        self._aaa = value


    def to_alipay_dict(self):
        params = dict()
        if self.aaa:
            if hasattr(self.aaa, 'to_alipay_dict'):
                params['aaa'] = self.aaa.to_alipay_dict()
            else:
                params['aaa'] = self.aaa
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityAppinfoQueryModel()
        if 'aaa' in d:
            o.aaa = d['aaa']
        return o


