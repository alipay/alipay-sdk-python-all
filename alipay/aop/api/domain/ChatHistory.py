#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChatHistory(object):

    def __init__(self):
        self._answer = None
        self._question = None
        self._time = None

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value):
        self._answer = value
    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, value):
        self._question = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value


    def to_alipay_dict(self):
        params = dict()
        if self.answer:
            if hasattr(self.answer, 'to_alipay_dict'):
                params['answer'] = self.answer.to_alipay_dict()
            else:
                params['answer'] = self.answer
        if self.question:
            if hasattr(self.question, 'to_alipay_dict'):
                params['question'] = self.question.to_alipay_dict()
            else:
                params['question'] = self.question
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChatHistory()
        if 'answer' in d:
            o.answer = d['answer']
        if 'question' in d:
            o.question = d['question']
        if 'time' in d:
            o.time = d['time']
        return o


