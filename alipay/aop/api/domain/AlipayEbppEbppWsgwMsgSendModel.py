#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppEbppWsgwMsgSendModel(object):

    def __init__(self):
        self._province_code = None
        self._secret_content = None
        self._type_code = None

    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def secret_content(self):
        return self._secret_content

    @secret_content.setter
    def secret_content(self, value):
        self._secret_content = value
    @property
    def type_code(self):
        return self._type_code

    @type_code.setter
    def type_code(self, value):
        self._type_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.secret_content:
            if hasattr(self.secret_content, 'to_alipay_dict'):
                params['secret_content'] = self.secret_content.to_alipay_dict()
            else:
                params['secret_content'] = self.secret_content
        if self.type_code:
            if hasattr(self.type_code, 'to_alipay_dict'):
                params['type_code'] = self.type_code.to_alipay_dict()
            else:
                params['type_code'] = self.type_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppEbppWsgwMsgSendModel()
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'secret_content' in d:
            o.secret_content = d['secret_content']
        if 'type_code' in d:
            o.type_code = d['type_code']
        return o


