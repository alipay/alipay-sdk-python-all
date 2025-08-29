#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsuranceUserSignModel(object):

    def __init__(self):
        self._biz_type = None
        self._query_token = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def query_token(self):
        return self._query_token

    @query_token.setter
    def query_token(self, value):
        self._query_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.query_token:
            if hasattr(self.query_token, 'to_alipay_dict'):
                params['query_token'] = self.query_token.to_alipay_dict()
            else:
                params['query_token'] = self.query_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceUserSignModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'query_token' in d:
            o.query_token = d['query_token']
        return o


