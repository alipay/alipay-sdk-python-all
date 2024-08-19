#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIcontroldcUserQueryModel(object):

    def __init__(self):
        self._dev_identifier = None
        self._dev_token = None

    @property
    def dev_identifier(self):
        return self._dev_identifier

    @dev_identifier.setter
    def dev_identifier(self, value):
        self._dev_identifier = value
    @property
    def dev_token(self):
        return self._dev_token

    @dev_token.setter
    def dev_token(self, value):
        self._dev_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.dev_identifier:
            if hasattr(self.dev_identifier, 'to_alipay_dict'):
                params['dev_identifier'] = self.dev_identifier.to_alipay_dict()
            else:
                params['dev_identifier'] = self.dev_identifier
        if self.dev_token:
            if hasattr(self.dev_token, 'to_alipay_dict'):
                params['dev_token'] = self.dev_token.to_alipay_dict()
            else:
                params['dev_token'] = self.dev_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIcontroldcUserQueryModel()
        if 'dev_identifier' in d:
            o.dev_identifier = d['dev_identifier']
        if 'dev_token' in d:
            o.dev_token = d['dev_token']
        return o


