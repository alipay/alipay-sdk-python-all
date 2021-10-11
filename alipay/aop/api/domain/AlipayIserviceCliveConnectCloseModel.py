#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCliveConnectCloseModel(object):

    def __init__(self):
        self._conversation_id = None
        self._src = None
        self._visitor_token = None

    @property
    def conversation_id(self):
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, value):
        self._conversation_id = value
    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, value):
        self._src = value
    @property
    def visitor_token(self):
        return self._visitor_token

    @visitor_token.setter
    def visitor_token(self, value):
        self._visitor_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.conversation_id:
            if hasattr(self.conversation_id, 'to_alipay_dict'):
                params['conversation_id'] = self.conversation_id.to_alipay_dict()
            else:
                params['conversation_id'] = self.conversation_id
        if self.src:
            if hasattr(self.src, 'to_alipay_dict'):
                params['src'] = self.src.to_alipay_dict()
            else:
                params['src'] = self.src
        if self.visitor_token:
            if hasattr(self.visitor_token, 'to_alipay_dict'):
                params['visitor_token'] = self.visitor_token.to_alipay_dict()
            else:
                params['visitor_token'] = self.visitor_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCliveConnectCloseModel()
        if 'conversation_id' in d:
            o.conversation_id = d['conversation_id']
        if 'src' in d:
            o.src = d['src']
        if 'visitor_token' in d:
            o.visitor_token = d['visitor_token']
        return o


