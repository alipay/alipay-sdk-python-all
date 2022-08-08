#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppTestagainCreateModel(object):

    def __init__(self):
        self._xxxxxx = None

    @property
    def xxxxxx(self):
        return self._xxxxxx

    @xxxxxx.setter
    def xxxxxx(self, value):
        self._xxxxxx = value


    def to_alipay_dict(self):
        params = dict()
        if self.xxxxxx:
            if hasattr(self.xxxxxx, 'to_alipay_dict'):
                params['xxxxxx'] = self.xxxxxx.to_alipay_dict()
            else:
                params['xxxxxx'] = self.xxxxxx
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppTestagainCreateModel()
        if 'xxxxxx' in d:
            o.xxxxxx = d['xxxxxx']
        return o


