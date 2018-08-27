#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdXwbtestprodQueryModel(object):

    def __init__(self):
        self._province_code = None
        self._qwe_dfgfd = None

    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def qwe_dfgfd(self):
        return self._qwe_dfgfd

    @qwe_dfgfd.setter
    def qwe_dfgfd(self, value):
        self._qwe_dfgfd = value


    def to_alipay_dict(self):
        params = dict()
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.qwe_dfgfd:
            if hasattr(self.qwe_dfgfd, 'to_alipay_dict'):
                params['qwe_dfgfd'] = self.qwe_dfgfd.to_alipay_dict()
            else:
                params['qwe_dfgfd'] = self.qwe_dfgfd
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdXwbtestprodQueryModel()
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'qwe_dfgfd' in d:
            o.qwe_dfgfd = d['qwe_dfgfd']
        return o


