#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradePayoffQueryModel(object):

    def __init__(self):
        self._bbb = None
        self._ccc = None

    @property
    def bbb(self):
        return self._bbb

    @bbb.setter
    def bbb(self, value):
        self._bbb = value
    @property
    def ccc(self):
        return self._ccc

    @ccc.setter
    def ccc(self, value):
        self._ccc = value


    def to_alipay_dict(self):
        params = dict()
        if self.bbb:
            if hasattr(self.bbb, 'to_alipay_dict'):
                params['bbb'] = self.bbb.to_alipay_dict()
            else:
                params['bbb'] = self.bbb
        if self.ccc:
            if hasattr(self.ccc, 'to_alipay_dict'):
                params['ccc'] = self.ccc.to_alipay_dict()
            else:
                params['ccc'] = self.ccc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradePayoffQueryModel()
        if 'bbb' in d:
            o.bbb = d['bbb']
        if 'ccc' in d:
            o.ccc = d['ccc']
        return o


