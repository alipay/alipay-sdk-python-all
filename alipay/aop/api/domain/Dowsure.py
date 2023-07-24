#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Dowsure(object):

    def __init__(self):
        self._application_code = None

    @property
    def application_code(self):
        return self._application_code

    @application_code.setter
    def application_code(self, value):
        self._application_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.application_code:
            if hasattr(self.application_code, 'to_alipay_dict'):
                params['application_code'] = self.application_code.to_alipay_dict()
            else:
                params['application_code'] = self.application_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Dowsure()
        if 'application_code' in d:
            o.application_code = d['application_code']
        return o


