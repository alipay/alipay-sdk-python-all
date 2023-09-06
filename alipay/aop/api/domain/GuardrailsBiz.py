#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GuardrailsBiz(object):

    def __init__(self):
        self._business_code = None
        self._business_msg = None

    @property
    def business_code(self):
        return self._business_code

    @business_code.setter
    def business_code(self, value):
        self._business_code = value
    @property
    def business_msg(self):
        return self._business_msg

    @business_msg.setter
    def business_msg(self, value):
        self._business_msg = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_code:
            if hasattr(self.business_code, 'to_alipay_dict'):
                params['business_code'] = self.business_code.to_alipay_dict()
            else:
                params['business_code'] = self.business_code
        if self.business_msg:
            if hasattr(self.business_msg, 'to_alipay_dict'):
                params['business_msg'] = self.business_msg.to_alipay_dict()
            else:
                params['business_msg'] = self.business_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GuardrailsBiz()
        if 'business_code' in d:
            o.business_code = d['business_code']
        if 'business_msg' in d:
            o.business_msg = d['business_msg']
        return o


