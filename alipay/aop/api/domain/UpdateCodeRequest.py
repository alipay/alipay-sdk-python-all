#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UpdateCodeRequest(object):

    def __init__(self):
        self._action = None
        self._biz_id = None
        self._code_token = None
        self._context_data = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def code_token(self):
        return self._code_token

    @code_token.setter
    def code_token(self, value):
        self._code_token = value
    @property
    def context_data(self):
        return self._context_data

    @context_data.setter
    def context_data(self, value):
        self._context_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.code_token:
            if hasattr(self.code_token, 'to_alipay_dict'):
                params['code_token'] = self.code_token.to_alipay_dict()
            else:
                params['code_token'] = self.code_token
        if self.context_data:
            if hasattr(self.context_data, 'to_alipay_dict'):
                params['context_data'] = self.context_data.to_alipay_dict()
            else:
                params['context_data'] = self.context_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UpdateCodeRequest()
        if 'action' in d:
            o.action = d['action']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'code_token' in d:
            o.code_token = d['code_token']
        if 'context_data' in d:
            o.context_data = d['context_data']
        return o


