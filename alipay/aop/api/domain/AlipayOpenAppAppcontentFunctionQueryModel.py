#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppAppcontentFunctionQueryModel(object):

    def __init__(self):
        self._service_code = None

    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppAppcontentFunctionQueryModel()
        if 'service_code' in d:
            o.service_code = d['service_code']
        return o


