#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserServiceCardConsultModel(object):

    def __init__(self):
        self._context = None
        self._context_id = None
        self._intent = None
        self._message_id = None
        self._open_id = None
        self._query = None
        self._user_id = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        self._context = value
    @property
    def context_id(self):
        return self._context_id

    @context_id.setter
    def context_id(self, value):
        self._context_id = value
    @property
    def intent(self):
        return self._intent

    @intent.setter
    def intent(self, value):
        self._intent = value
    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, value):
        self._message_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.context:
            if hasattr(self.context, 'to_alipay_dict'):
                params['context'] = self.context.to_alipay_dict()
            else:
                params['context'] = self.context
        if self.context_id:
            if hasattr(self.context_id, 'to_alipay_dict'):
                params['context_id'] = self.context_id.to_alipay_dict()
            else:
                params['context_id'] = self.context_id
        if self.intent:
            if hasattr(self.intent, 'to_alipay_dict'):
                params['intent'] = self.intent.to_alipay_dict()
            else:
                params['intent'] = self.intent
        if self.message_id:
            if hasattr(self.message_id, 'to_alipay_dict'):
                params['message_id'] = self.message_id.to_alipay_dict()
            else:
                params['message_id'] = self.message_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserServiceCardConsultModel()
        if 'context' in d:
            o.context = d['context']
        if 'context_id' in d:
            o.context_id = d['context_id']
        if 'intent' in d:
            o.intent = d['intent']
        if 'message_id' in d:
            o.message_id = d['message_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'query' in d:
            o.query = d['query']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


