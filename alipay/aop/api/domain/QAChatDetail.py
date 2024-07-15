#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RobotAnswer import RobotAnswer


class QAChatDetail(object):

    def __init__(self):
        self._answer = None
        self._answer_type = None
        self._chat_uuid = None
        self._local_timestamp = None
        self._query = None
        self._vote_type = None

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value):
        if isinstance(value, RobotAnswer):
            self._answer = value
        else:
            self._answer = RobotAnswer.from_alipay_dict(value)
    @property
    def answer_type(self):
        return self._answer_type

    @answer_type.setter
    def answer_type(self, value):
        self._answer_type = value
    @property
    def chat_uuid(self):
        return self._chat_uuid

    @chat_uuid.setter
    def chat_uuid(self, value):
        self._chat_uuid = value
    @property
    def local_timestamp(self):
        return self._local_timestamp

    @local_timestamp.setter
    def local_timestamp(self, value):
        self._local_timestamp = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
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
        if self.answer_type:
            if hasattr(self.answer_type, 'to_alipay_dict'):
                params['answer_type'] = self.answer_type.to_alipay_dict()
            else:
                params['answer_type'] = self.answer_type
        if self.chat_uuid:
            if hasattr(self.chat_uuid, 'to_alipay_dict'):
                params['chat_uuid'] = self.chat_uuid.to_alipay_dict()
            else:
                params['chat_uuid'] = self.chat_uuid
        if self.local_timestamp:
            if hasattr(self.local_timestamp, 'to_alipay_dict'):
                params['local_timestamp'] = self.local_timestamp.to_alipay_dict()
            else:
                params['local_timestamp'] = self.local_timestamp
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
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
        o = QAChatDetail()
        if 'answer' in d:
            o.answer = d['answer']
        if 'answer_type' in d:
            o.answer_type = d['answer_type']
        if 'chat_uuid' in d:
            o.chat_uuid = d['chat_uuid']
        if 'local_timestamp' in d:
            o.local_timestamp = d['local_timestamp']
        if 'query' in d:
            o.query = d['query']
        if 'vote_type' in d:
            o.vote_type = d['vote_type']
        return o


