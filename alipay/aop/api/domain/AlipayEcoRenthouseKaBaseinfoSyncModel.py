#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoRenthouseKaBaseinfoSyncModel(object):

    def __init__(self):
        self._ka_code = None
        self._ka_name = None

    @property
    def ka_code(self):
        return self._ka_code

    @ka_code.setter
    def ka_code(self, value):
        self._ka_code = value
    @property
    def ka_name(self):
        return self._ka_name

    @ka_name.setter
    def ka_name(self, value):
        self._ka_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ka_code:
            if hasattr(self.ka_code, 'to_alipay_dict'):
                params['ka_code'] = self.ka_code.to_alipay_dict()
            else:
                params['ka_code'] = self.ka_code
        if self.ka_name:
            if hasattr(self.ka_name, 'to_alipay_dict'):
                params['ka_name'] = self.ka_name.to_alipay_dict()
            else:
                params['ka_name'] = self.ka_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoRenthouseKaBaseinfoSyncModel()
        if 'ka_code' in d:
            o.ka_code = d['ka_code']
        if 'ka_name' in d:
            o.ka_name = d['ka_name']
        return o


