#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NbMessage(object):

    def __init__(self):
        self._agent_id = None
        self._answer = None
        self._conversation_id = None
        self._create_time = None
        self._id = None
        self._inputs = None
        self._media_type = None
        self._query = None
        self._related_questions = None
        self._request_id = None
        self._status = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value):
        self._answer = value
    @property
    def conversation_id(self):
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, value):
        self._conversation_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def inputs(self):
        return self._inputs

    @inputs.setter
    def inputs(self, value):
        self._inputs = value
    @property
    def media_type(self):
        return self._media_type

    @media_type.setter
    def media_type(self, value):
        self._media_type = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def related_questions(self):
        return self._related_questions

    @related_questions.setter
    def related_questions(self, value):
        if isinstance(value, list):
            self._related_questions = list()
            for i in value:
                self._related_questions.append(i)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.answer:
            if hasattr(self.answer, 'to_alipay_dict'):
                params['answer'] = self.answer.to_alipay_dict()
            else:
                params['answer'] = self.answer
        if self.conversation_id:
            if hasattr(self.conversation_id, 'to_alipay_dict'):
                params['conversation_id'] = self.conversation_id.to_alipay_dict()
            else:
                params['conversation_id'] = self.conversation_id
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.inputs:
            if hasattr(self.inputs, 'to_alipay_dict'):
                params['inputs'] = self.inputs.to_alipay_dict()
            else:
                params['inputs'] = self.inputs
        if self.media_type:
            if hasattr(self.media_type, 'to_alipay_dict'):
                params['media_type'] = self.media_type.to_alipay_dict()
            else:
                params['media_type'] = self.media_type
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.related_questions:
            if isinstance(self.related_questions, list):
                for i in range(0, len(self.related_questions)):
                    element = self.related_questions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_questions[i] = element.to_alipay_dict()
            if hasattr(self.related_questions, 'to_alipay_dict'):
                params['related_questions'] = self.related_questions.to_alipay_dict()
            else:
                params['related_questions'] = self.related_questions
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NbMessage()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'answer' in d:
            o.answer = d['answer']
        if 'conversation_id' in d:
            o.conversation_id = d['conversation_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'id' in d:
            o.id = d['id']
        if 'inputs' in d:
            o.inputs = d['inputs']
        if 'media_type' in d:
            o.media_type = d['media_type']
        if 'query' in d:
            o.query = d['query']
        if 'related_questions' in d:
            o.related_questions = d['related_questions']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'status' in d:
            o.status = d['status']
        return o


