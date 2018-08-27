#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdUmidQueryModel(object):

    def __init__(self):
        self._token_id = None

    @property
    def token_id(self):
        return self._token_id

    @token_id.setter
    def token_id(self, value):
        self._token_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.token_id:
            if hasattr(self.token_id, 'to_alipay_dict'):
                params['token_id'] = self.token_id.to_alipay_dict()
            else:
                params['token_id'] = self.token_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdUmidQueryModel()
        if 'token_id' in d:
            o.token_id = d['token_id']
        return o


