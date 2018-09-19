#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransAacollectBatchQueryModel(object):

    def __init__(self):
        self._batch_no = None
        self._batch_token = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def batch_token(self):
        return self._batch_token

    @batch_token.setter
    def batch_token(self, value):
        self._batch_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.batch_token:
            if hasattr(self.batch_token, 'to_alipay_dict'):
                params['batch_token'] = self.batch_token.to_alipay_dict()
            else:
                params['batch_token'] = self.batch_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransAacollectBatchQueryModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'batch_token' in d:
            o.batch_token = d['batch_token']
        return o


