#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransAacollectBatchCloseModel(object):

    def __init__(self):
        self._batch_no = None
        self._batch_token = None
        self._current_user_id = None

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
    @property
    def current_user_id(self):
        return self._current_user_id

    @current_user_id.setter
    def current_user_id(self, value):
        self._current_user_id = value


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
        if self.current_user_id:
            if hasattr(self.current_user_id, 'to_alipay_dict'):
                params['current_user_id'] = self.current_user_id.to_alipay_dict()
            else:
                params['current_user_id'] = self.current_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransAacollectBatchCloseModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'batch_token' in d:
            o.batch_token = d['batch_token']
        if 'current_user_id' in d:
            o.current_user_id = d['current_user_id']
        return o


