#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerbaseinfoParameterVerifyModel(object):

    def __init__(self):
        self._verify_type = None
        self._verify_value = None

    @property
    def verify_type(self):
        return self._verify_type

    @verify_type.setter
    def verify_type(self, value):
        self._verify_type = value
    @property
    def verify_value(self):
        return self._verify_value

    @verify_value.setter
    def verify_value(self, value):
        self._verify_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.verify_type:
            if hasattr(self.verify_type, 'to_alipay_dict'):
                params['verify_type'] = self.verify_type.to_alipay_dict()
            else:
                params['verify_type'] = self.verify_type
        if self.verify_value:
            if hasattr(self.verify_value, 'to_alipay_dict'):
                params['verify_value'] = self.verify_value.to_alipay_dict()
            else:
                params['verify_value'] = self.verify_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerbaseinfoParameterVerifyModel()
        if 'verify_type' in d:
            o.verify_type = d['verify_type']
        if 'verify_value' in d:
            o.verify_value = d['verify_value']
        return o


