#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Terminal import Terminal


class AlipayOpenStsTokenGetModel(object):

    def __init__(self):
        self._security_token = None
        self._terminal = None

    @property
    def security_token(self):
        return self._security_token

    @security_token.setter
    def security_token(self, value):
        self._security_token = value
    @property
    def terminal(self):
        return self._terminal

    @terminal.setter
    def terminal(self, value):
        if isinstance(value, Terminal):
            self._terminal = value
        else:
            self._terminal = Terminal.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.security_token:
            if hasattr(self.security_token, 'to_alipay_dict'):
                params['security_token'] = self.security_token.to_alipay_dict()
            else:
                params['security_token'] = self.security_token
        if self.terminal:
            if hasattr(self.terminal, 'to_alipay_dict'):
                params['terminal'] = self.terminal.to_alipay_dict()
            else:
                params['terminal'] = self.terminal
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenStsTokenGetModel()
        if 'security_token' in d:
            o.security_token = d['security_token']
        if 'terminal' in d:
            o.terminal = d['terminal']
        return o


