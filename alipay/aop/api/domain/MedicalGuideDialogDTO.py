#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalGuideContentDTO import MedicalGuideContentDTO


class MedicalGuideDialogDTO(object):

    def __init__(self):
        self._chat_id = None
        self._content = None
        self._question = None
        self._question_type = None

    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, MedicalGuideContentDTO):
            self._content = value
        else:
            self._content = MedicalGuideContentDTO.from_alipay_dict(value)
    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, value):
        self._question = value
    @property
    def question_type(self):
        return self._question_type

    @question_type.setter
    def question_type(self, value):
        self._question_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.question:
            if hasattr(self.question, 'to_alipay_dict'):
                params['question'] = self.question.to_alipay_dict()
            else:
                params['question'] = self.question
        if self.question_type:
            if hasattr(self.question_type, 'to_alipay_dict'):
                params['question_type'] = self.question_type.to_alipay_dict()
            else:
                params['question_type'] = self.question_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalGuideDialogDTO()
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'content' in d:
            o.content = d['content']
        if 'question' in d:
            o.question = d['question']
        if 'question_type' in d:
            o.question_type = d['question_type']
        return o


