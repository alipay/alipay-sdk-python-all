#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustrySecurityAnswerCheckModel(object):

    def __init__(self):
        self._answer = None
        self._answer_flow_id = None
        self._answer_format = None
        self._answer_index = None
        self._answer_type = None
        self._chat_id = None
        self._identify_id = None
        self._open_id = None
        self._question = None
        self._question_format = None
        self._session_id = None
        self._user_id = None

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value):
        self._answer = value
    @property
    def answer_flow_id(self):
        return self._answer_flow_id

    @answer_flow_id.setter
    def answer_flow_id(self, value):
        self._answer_flow_id = value
    @property
    def answer_format(self):
        return self._answer_format

    @answer_format.setter
    def answer_format(self, value):
        self._answer_format = value
    @property
    def answer_index(self):
        return self._answer_index

    @answer_index.setter
    def answer_index(self, value):
        self._answer_index = value
    @property
    def answer_type(self):
        return self._answer_type

    @answer_type.setter
    def answer_type(self, value):
        self._answer_type = value
    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def identify_id(self):
        return self._identify_id

    @identify_id.setter
    def identify_id(self, value):
        self._identify_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, value):
        self._question = value
    @property
    def question_format(self):
        return self._question_format

    @question_format.setter
    def question_format(self, value):
        self._question_format = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.answer:
            if hasattr(self.answer, 'to_alipay_dict'):
                params['answer'] = self.answer.to_alipay_dict()
            else:
                params['answer'] = self.answer
        if self.answer_flow_id:
            if hasattr(self.answer_flow_id, 'to_alipay_dict'):
                params['answer_flow_id'] = self.answer_flow_id.to_alipay_dict()
            else:
                params['answer_flow_id'] = self.answer_flow_id
        if self.answer_format:
            if hasattr(self.answer_format, 'to_alipay_dict'):
                params['answer_format'] = self.answer_format.to_alipay_dict()
            else:
                params['answer_format'] = self.answer_format
        if self.answer_index:
            if hasattr(self.answer_index, 'to_alipay_dict'):
                params['answer_index'] = self.answer_index.to_alipay_dict()
            else:
                params['answer_index'] = self.answer_index
        if self.answer_type:
            if hasattr(self.answer_type, 'to_alipay_dict'):
                params['answer_type'] = self.answer_type.to_alipay_dict()
            else:
                params['answer_type'] = self.answer_type
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
        if self.identify_id:
            if hasattr(self.identify_id, 'to_alipay_dict'):
                params['identify_id'] = self.identify_id.to_alipay_dict()
            else:
                params['identify_id'] = self.identify_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.question:
            if hasattr(self.question, 'to_alipay_dict'):
                params['question'] = self.question.to_alipay_dict()
            else:
                params['question'] = self.question
        if self.question_format:
            if hasattr(self.question_format, 'to_alipay_dict'):
                params['question_format'] = self.question_format.to_alipay_dict()
            else:
                params['question_format'] = self.question_format
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
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
        o = AlipayEbppIndustrySecurityAnswerCheckModel()
        if 'answer' in d:
            o.answer = d['answer']
        if 'answer_flow_id' in d:
            o.answer_flow_id = d['answer_flow_id']
        if 'answer_format' in d:
            o.answer_format = d['answer_format']
        if 'answer_index' in d:
            o.answer_index = d['answer_index']
        if 'answer_type' in d:
            o.answer_type = d['answer_type']
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'identify_id' in d:
            o.identify_id = d['identify_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'question' in d:
            o.question = d['question']
        if 'question_format' in d:
            o.question_format = d['question_format']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


