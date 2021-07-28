#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditUserInfoShareQueryModel(object):

    def __init__(self):
        self._access_token = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_token:
            if hasattr(self.access_token, 'to_alipay_dict'):
                params['access_token'] = self.access_token.to_alipay_dict()
            else:
                params['access_token'] = self.access_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditUserInfoShareQueryModel()
        if 'access_token' in d:
            o.access_token = d['access_token']
        return o


