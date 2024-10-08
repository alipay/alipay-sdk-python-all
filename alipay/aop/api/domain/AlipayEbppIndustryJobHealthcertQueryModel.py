#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryJobHealthcertQueryModel(object):

    def __init__(self):
        self._certify_token = None

    @property
    def certify_token(self):
        return self._certify_token

    @certify_token.setter
    def certify_token(self, value):
        self._certify_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.certify_token:
            if hasattr(self.certify_token, 'to_alipay_dict'):
                params['certify_token'] = self.certify_token.to_alipay_dict()
            else:
                params['certify_token'] = self.certify_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryJobHealthcertQueryModel()
        if 'certify_token' in d:
            o.certify_token = d['certify_token']
        return o


