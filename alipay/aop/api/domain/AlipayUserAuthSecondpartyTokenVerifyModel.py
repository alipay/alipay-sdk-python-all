#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAuthSecondpartyTokenVerifyModel(object):

    def __init__(self):
        self._second_party_token = None
        self._source = None

    @property
    def second_party_token(self):
        return self._second_party_token

    @second_party_token.setter
    def second_party_token(self, value):
        self._second_party_token = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.second_party_token:
            if hasattr(self.second_party_token, 'to_alipay_dict'):
                params['second_party_token'] = self.second_party_token.to_alipay_dict()
            else:
                params['second_party_token'] = self.second_party_token
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAuthSecondpartyTokenVerifyModel()
        if 'second_party_token' in d:
            o.second_party_token = d['second_party_token']
        if 'source' in d:
            o.source = d['source']
        return o


