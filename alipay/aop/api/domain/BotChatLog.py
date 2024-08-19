#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BotAnswer import BotAnswer


class BotChatLog(object):

    def __init__(self):
        self._answer = None
        self._ask_time = None
        self._chat_id = None
        self._query = None
        self._session_id = None
        self._vote_type = None

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value):
        if isinstance(value, BotAnswer):
            self._answer = value
        else:
            self._answer = BotAnswer.from_alipay_dict(value)
    @property
    def ask_time(self):
        return self._ask_time

    @ask_time.setter
    def ask_time(self, value):
        self._ask_time = value
    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def vote_type(self):
        return self._vote_type

    @vote_type.setter
    def vote_type(self, value):
        self._vote_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.answer:
            if hasattr(self.answer, 'to_alipay_dict'):
                params['answer'] = self.answer.to_alipay_dict()
            else:
                params['answer'] = self.answer
        if self.ask_time:
            if hasattr(self.ask_time, 'to_alipay_dict'):
                params['ask_time'] = self.ask_time.to_alipay_dict()
            else:
                params['ask_time'] = self.ask_time
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.vote_type:
            if hasattr(self.vote_type, 'to_alipay_dict'):
                params['vote_type'] = self.vote_type.to_alipay_dict()
            else:
                params['vote_type'] = self.vote_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BotChatLog()
        if 'answer' in d:
            o.answer = d['answer']
        if 'ask_time' in d:
            o.ask_time = d['ask_time']
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'query' in d:
            o.query = d['query']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'vote_type' in d:
            o.vote_type = d['vote_type']
        return o


