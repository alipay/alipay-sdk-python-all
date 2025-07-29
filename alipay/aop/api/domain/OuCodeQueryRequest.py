#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OuCodeQueryRequest(object):

    def __init__(self):
        self._ou_code = None

    @property
    def ou_code(self):
        return self._ou_code

    @ou_code.setter
    def ou_code(self, value):
        self._ou_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.ou_code:
            if hasattr(self.ou_code, 'to_alipay_dict'):
                params['ou_code'] = self.ou_code.to_alipay_dict()
            else:
                params['ou_code'] = self.ou_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OuCodeQueryRequest()
        if 'ou_code' in d:
            o.ou_code = d['ou_code']
        return o


