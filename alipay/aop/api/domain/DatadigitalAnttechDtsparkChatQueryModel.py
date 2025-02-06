#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAnttechDtsparkChatQueryModel(object):

    def __init__(self):
        self._agent_id = None
        self._question = None
        self._secret = None
        self._session_id = None
        self._source = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, value):
        self._question = value
    @property
    def secret(self):
        return self._secret

    @secret.setter
    def secret(self, value):
        self._secret = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.question:
            if hasattr(self.question, 'to_alipay_dict'):
                params['question'] = self.question.to_alipay_dict()
            else:
                params['question'] = self.question
        if self.secret:
            if hasattr(self.secret, 'to_alipay_dict'):
                params['secret'] = self.secret.to_alipay_dict()
            else:
                params['secret'] = self.secret
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
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
        o = DatadigitalAnttechDtsparkChatQueryModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'question' in d:
            o.question = d['question']
        if 'secret' in d:
            o.secret = d['secret']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'source' in d:
            o.source = d['source']
        return o


