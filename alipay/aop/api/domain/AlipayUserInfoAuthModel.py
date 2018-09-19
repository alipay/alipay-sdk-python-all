#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserInfoAuthModel(object):

    def __init__(self):
        self._scopes = None
        self._state = None

    @property
    def scopes(self):
        return self._scopes

    @scopes.setter
    def scopes(self, value):
        if isinstance(value, list):
            self._scopes = list()
            for i in value:
                self._scopes.append(i)
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value


    def to_alipay_dict(self):
        params = dict()
        if self.scopes:
            if isinstance(self.scopes, list):
                for i in range(0, len(self.scopes)):
                    element = self.scopes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scopes[i] = element.to_alipay_dict()
            if hasattr(self.scopes, 'to_alipay_dict'):
                params['scopes'] = self.scopes.to_alipay_dict()
            else:
                params['scopes'] = self.scopes
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserInfoAuthModel()
        if 'scopes' in d:
            o.scopes = d['scopes']
        if 'state' in d:
            o.state = d['state']
        return o


