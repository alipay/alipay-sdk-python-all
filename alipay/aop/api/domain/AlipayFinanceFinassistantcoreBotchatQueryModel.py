#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinanceFinassistantcoreBotchatQueryModel(object):

    def __init__(self):
        self._chat = None
        self._question = None
        self._session_id = None
        self._user_type = None

    @property
    def chat(self):
        return self._chat

    @chat.setter
    def chat(self, value):
        self._chat = value
    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, value):
        self._question = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.chat:
            if hasattr(self.chat, 'to_alipay_dict'):
                params['chat'] = self.chat.to_alipay_dict()
            else:
                params['chat'] = self.chat
        if self.question:
            if hasattr(self.question, 'to_alipay_dict'):
                params['question'] = self.question.to_alipay_dict()
            else:
                params['question'] = self.question
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinanceFinassistantcoreBotchatQueryModel()
        if 'chat' in d:
            o.chat = d['chat']
        if 'question' in d:
            o.question = d['question']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


