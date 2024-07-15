#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemFrequentQA(object):

    def __init__(self):
        self._answer = None
        self._question = None

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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemFrequentQA()
        if 'answer' in d:
            o.answer = d['answer']
        if 'question' in d:
            o.question = d['question']
        return o


