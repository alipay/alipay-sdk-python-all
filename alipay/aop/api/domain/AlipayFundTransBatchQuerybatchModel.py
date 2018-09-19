#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransBatchQuerybatchModel(object):

    def __init__(self):
        self._batch_no = None
        self._token = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.token:
            if hasattr(self.token, 'to_alipay_dict'):
                params['token'] = self.token.to_alipay_dict()
            else:
                params['token'] = self.token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransBatchQuerybatchModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'token' in d:
            o.token = d['token']
        return o


