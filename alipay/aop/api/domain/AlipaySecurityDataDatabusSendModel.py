#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityDataDatabusSendModel(object):

    def __init__(self):
        self._security_content = None
        self._security_sign = None

    @property
    def security_content(self):
        return self._security_content

    @security_content.setter
    def security_content(self, value):
        self._security_content = value
    @property
    def security_sign(self):
        return self._security_sign

    @security_sign.setter
    def security_sign(self, value):
        self._security_sign = value


    def to_alipay_dict(self):
        params = dict()
        if self.security_content:
            if hasattr(self.security_content, 'to_alipay_dict'):
                params['security_content'] = self.security_content.to_alipay_dict()
            else:
                params['security_content'] = self.security_content
        if self.security_sign:
            if hasattr(self.security_sign, 'to_alipay_dict'):
                params['security_sign'] = self.security_sign.to_alipay_dict()
            else:
                params['security_sign'] = self.security_sign
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataDatabusSendModel()
        if 'security_content' in d:
            o.security_content = d['security_content']
        if 'security_sign' in d:
            o.security_sign = d['security_sign']
        return o


