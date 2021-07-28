#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AuthenticationResult(object):

    def __init__(self):
        self._authentication_data = None
        self._authentication_mechanism = None

    @property
    def authentication_data(self):
        return self._authentication_data

    @authentication_data.setter
    def authentication_data(self, value):
        self._authentication_data = value
    @property
    def authentication_mechanism(self):
        return self._authentication_mechanism

    @authentication_mechanism.setter
    def authentication_mechanism(self, value):
        self._authentication_mechanism = value


    def to_alipay_dict(self):
        params = dict()
        if self.authentication_data:
            if hasattr(self.authentication_data, 'to_alipay_dict'):
                params['authentication_data'] = self.authentication_data.to_alipay_dict()
            else:
                params['authentication_data'] = self.authentication_data
        if self.authentication_mechanism:
            if hasattr(self.authentication_mechanism, 'to_alipay_dict'):
                params['authentication_mechanism'] = self.authentication_mechanism.to_alipay_dict()
            else:
                params['authentication_mechanism'] = self.authentication_mechanism
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthenticationResult()
        if 'authentication_data' in d:
            o.authentication_data = d['authentication_data']
        if 'authentication_mechanism' in d:
            o.authentication_mechanism = d['authentication_mechanism']
        return o


