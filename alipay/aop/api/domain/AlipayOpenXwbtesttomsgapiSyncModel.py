#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenXwbtesttomsgapiSyncModel(object):

    def __init__(self):
        self._xwb = None

    @property
    def xwb(self):
        return self._xwb

    @xwb.setter
    def xwb(self, value):
        self._xwb = value


    def to_alipay_dict(self):
        params = dict()
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
        o = AlipayOpenXwbtesttomsgapiSyncModel()
        if 'xwb' in d:
            o.xwb = d['xwb']
        return o


