#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIsponetestComputertestQuickcreateModel(object):

    def __init__(self):
        self._sssss = None
        self._xxxtest = None

    @property
    def sssss(self):
        return self._sssss

    @sssss.setter
    def sssss(self, value):
        self._sssss = value
    @property
    def xxxtest(self):
        return self._xxxtest

    @xxxtest.setter
    def xxxtest(self, value):
        self._xxxtest = value


    def to_alipay_dict(self):
        params = dict()
        if self.sssss:
            if hasattr(self.sssss, 'to_alipay_dict'):
                params['sssss'] = self.sssss.to_alipay_dict()
            else:
                params['sssss'] = self.sssss
        if self.xxxtest:
            if hasattr(self.xxxtest, 'to_alipay_dict'):
                params['xxxtest'] = self.xxxtest.to_alipay_dict()
            else:
                params['xxxtest'] = self.xxxtest
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIsponetestComputertestQuickcreateModel()
        if 'sssss' in d:
            o.sssss = d['sssss']
        if 'xxxtest' in d:
            o.xxxtest = d['xxxtest']
        return o


