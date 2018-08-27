#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoRenthouseKaBaseinfoQueryModel(object):

    def __init__(self):
        self._ka_code = None

    @property
    def ka_code(self):
        return self._ka_code

    @ka_code.setter
    def ka_code(self, value):
        self._ka_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.ka_code:
            if hasattr(self.ka_code, 'to_alipay_dict'):
                params['ka_code'] = self.ka_code.to_alipay_dict()
            else:
                params['ka_code'] = self.ka_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoRenthouseKaBaseinfoQueryModel()
        if 'ka_code' in d:
            o.ka_code = d['ka_code']
        return o


