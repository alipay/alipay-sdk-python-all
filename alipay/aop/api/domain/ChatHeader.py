#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChatReference import ChatReference


class ChatHeader(object):

    def __init__(self):
        self._biz_trans_data = None
        self._question = None
        self._references = None
        self._related_questions = None
        self._request_id = None

    @property
    def biz_trans_data(self):
        return self._biz_trans_data

    @biz_trans_data.setter
    def biz_trans_data(self, value):
        self._biz_trans_data = value
    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, value):
        self._question = value
    @property
    def references(self):
        return self._references

    @references.setter
    def references(self, value):
        if isinstance(value, list):
            self._references = list()
            for i in value:
                if isinstance(i, ChatReference):
                    self._references.append(i)
                else:
                    self._references.append(ChatReference.from_alipay_dict(i))
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


    def to_alipay_dict(self):
        params = dict()
        if self.biz_trans_data:
            if hasattr(self.biz_trans_data, 'to_alipay_dict'):
                params['biz_trans_data'] = self.biz_trans_data.to_alipay_dict()
            else:
                params['biz_trans_data'] = self.biz_trans_data
        if self.question:
            if hasattr(self.question, 'to_alipay_dict'):
                params['question'] = self.question.to_alipay_dict()
            else:
                params['question'] = self.question
        if self.references:
            if isinstance(self.references, list):
                for i in range(0, len(self.references)):
                    element = self.references[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.references[i] = element.to_alipay_dict()
            if hasattr(self.references, 'to_alipay_dict'):
                params['references'] = self.references.to_alipay_dict()
            else:
                params['references'] = self.references
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChatHeader()
        if 'biz_trans_data' in d:
            o.biz_trans_data = d['biz_trans_data']
        if 'question' in d:
            o.question = d['question']
        if 'references' in d:
            o.references = d['references']
        if 'related_questions' in d:
            o.related_questions = d['related_questions']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


