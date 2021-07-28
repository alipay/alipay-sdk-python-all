#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankPaymentTradeQrcodeDeleteModel(object):

    def __init__(self):
        self._encrypt_token = None

    @property
    def encrypt_token(self):
        return self._encrypt_token

    @encrypt_token.setter
    def encrypt_token(self, value):
        self._encrypt_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.encrypt_token:
            if hasattr(self.encrypt_token, 'to_alipay_dict'):
                params['encrypt_token'] = self.encrypt_token.to_alipay_dict()
            else:
                params['encrypt_token'] = self.encrypt_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankPaymentTradeQrcodeDeleteModel()
        if 'encrypt_token' in d:
            o.encrypt_token = d['encrypt_token']
        return o


