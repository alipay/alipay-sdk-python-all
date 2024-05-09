#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneFinresearchConsultFeedbackCreateModel(object):

    def __init__(self):
        self._answer = None
        self._comment = None
        self._consult_id = None
        self._identity_id = None
        self._operate_type = None
        self._question = None
        self._session_id = None

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value):
        self._answer = value
    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
    @property
    def consult_id(self):
        return self._consult_id

    @consult_id.setter
    def consult_id(self, value):
        self._consult_id = value
    @property
    def identity_id(self):
        return self._identity_id

    @identity_id.setter
    def identity_id(self, value):
        self._identity_id = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.answer:
            if hasattr(self.answer, 'to_alipay_dict'):
                params['answer'] = self.answer.to_alipay_dict()
            else:
                params['answer'] = self.answer
        if self.comment:
            if hasattr(self.comment, 'to_alipay_dict'):
                params['comment'] = self.comment.to_alipay_dict()
            else:
                params['comment'] = self.comment
        if self.consult_id:
            if hasattr(self.consult_id, 'to_alipay_dict'):
                params['consult_id'] = self.consult_id.to_alipay_dict()
            else:
                params['consult_id'] = self.consult_id
        if self.identity_id:
            if hasattr(self.identity_id, 'to_alipay_dict'):
                params['identity_id'] = self.identity_id.to_alipay_dict()
            else:
                params['identity_id'] = self.identity_id
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneFinresearchConsultFeedbackCreateModel()
        if 'answer' in d:
            o.answer = d['answer']
        if 'comment' in d:
            o.comment = d['comment']
        if 'consult_id' in d:
            o.consult_id = d['consult_id']
        if 'identity_id' in d:
            o.identity_id = d['identity_id']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'question' in d:
            o.question = d['question']
        if 'session_id' in d:
            o.session_id = d['session_id']
        return o


