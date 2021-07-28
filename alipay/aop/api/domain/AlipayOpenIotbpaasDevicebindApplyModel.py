#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotbpaasDevicebindApplyModel(object):

    def __init__(self):
        self._bind_token = None
        self._type = None

    @property
    def bind_token(self):
        return self._bind_token

    @bind_token.setter
    def bind_token(self, value):
        self._bind_token = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_token:
            if hasattr(self.bind_token, 'to_alipay_dict'):
                params['bind_token'] = self.bind_token.to_alipay_dict()
            else:
                params['bind_token'] = self.bind_token
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotbpaasDevicebindApplyModel()
        if 'bind_token' in d:
            o.bind_token = d['bind_token']
        if 'type' in d:
            o.type = d['type']
        return o


