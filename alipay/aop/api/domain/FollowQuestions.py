#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Options import Options


class FollowQuestions(object):

    def __init__(self):
        self._follow_answer = None
        self._follow_question = None
        self._follow_question_no = None
        self._follow_question_type = None
        self._options = None

    @property
    def follow_answer(self):
        return self._follow_answer

    @follow_answer.setter
    def follow_answer(self, value):
        self._follow_answer = value
    @property
    def follow_question(self):
        return self._follow_question

    @follow_question.setter
    def follow_question(self, value):
        self._follow_question = value
    @property
    def follow_question_no(self):
        return self._follow_question_no

    @follow_question_no.setter
    def follow_question_no(self, value):
        self._follow_question_no = value
    @property
    def follow_question_type(self):
        return self._follow_question_type

    @follow_question_type.setter
    def follow_question_type(self, value):
        self._follow_question_type = value
    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        if isinstance(value, list):
            self._options = list()
            for i in value:
                if isinstance(i, Options):
                    self._options.append(i)
                else:
                    self._options.append(Options.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.follow_answer:
            if hasattr(self.follow_answer, 'to_alipay_dict'):
                params['follow_answer'] = self.follow_answer.to_alipay_dict()
            else:
                params['follow_answer'] = self.follow_answer
        if self.follow_question:
            if hasattr(self.follow_question, 'to_alipay_dict'):
                params['follow_question'] = self.follow_question.to_alipay_dict()
            else:
                params['follow_question'] = self.follow_question
        if self.follow_question_no:
            if hasattr(self.follow_question_no, 'to_alipay_dict'):
                params['follow_question_no'] = self.follow_question_no.to_alipay_dict()
            else:
                params['follow_question_no'] = self.follow_question_no
        if self.follow_question_type:
            if hasattr(self.follow_question_type, 'to_alipay_dict'):
                params['follow_question_type'] = self.follow_question_type.to_alipay_dict()
            else:
                params['follow_question_type'] = self.follow_question_type
        if self.options:
            if isinstance(self.options, list):
                for i in range(0, len(self.options)):
                    element = self.options[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.options[i] = element.to_alipay_dict()
            if hasattr(self.options, 'to_alipay_dict'):
                params['options'] = self.options.to_alipay_dict()
            else:
                params['options'] = self.options
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FollowQuestions()
        if 'follow_answer' in d:
            o.follow_answer = d['follow_answer']
        if 'follow_question' in d:
            o.follow_question = d['follow_question']
        if 'follow_question_no' in d:
            o.follow_question_no = d['follow_question_no']
        if 'follow_question_type' in d:
            o.follow_question_type = d['follow_question_type']
        if 'options' in d:
            o.options = d['options']
        return o


