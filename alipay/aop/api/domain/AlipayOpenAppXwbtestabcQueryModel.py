#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppXwbtestabcQueryModel(object):

    def __init__(self):
        self._testabc = None
        self._xwb = None

    @property
    def testabc(self):
        return self._testabc

    @testabc.setter
    def testabc(self, value):
        self._testabc = value
    @property
    def xwb(self):
        return self._xwb

    @xwb.setter
    def xwb(self, value):
        self._xwb = value


    def to_alipay_dict(self):
        params = dict()
        if self.testabc:
            if hasattr(self.testabc, 'to_alipay_dict'):
                params['testabc'] = self.testabc.to_alipay_dict()
            else:
                params['testabc'] = self.testabc
        if self.xwb:
            if hasattr(self.xwb, 'to_alipay_dict'):
                params['xwb'] = self.xwb.to_alipay_dict()
            else:
                params['xwb'] = self.xwb
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppXwbtestabcQueryModel()
        if 'testabc' in d:
            o.testabc = d['testabc']
        if 'xwb' in d:
            o.xwb = d['xwb']
        return o


