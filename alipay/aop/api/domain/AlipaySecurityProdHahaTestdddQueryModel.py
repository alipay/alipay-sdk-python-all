#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdHahaTestdddQueryModel(object):

    def __init__(self):
        self._haha = None

    @property
    def haha(self):
        return self._haha

    @haha.setter
    def haha(self, value):
        self._haha = value


    def to_alipay_dict(self):
        params = dict()
        if self.haha:
            if hasattr(self.haha, 'to_alipay_dict'):
                params['haha'] = self.haha.to_alipay_dict()
            else:
                params['haha'] = self.haha
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdHahaTestdddQueryModel()
        if 'haha' in d:
            o.haha = d['haha']
        return o


