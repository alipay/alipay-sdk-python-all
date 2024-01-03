#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalIndustrydataIntelligentdiagnosisSendModel(object):

    def __init__(self):
        self._chat_id = None
        self._open_id = None
        self._outer_user_no = None
        self._outer_user_type = None
        self._question = None
        self._question_type = None
        self._session_id = None
        self._source_type = None

    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def outer_user_no(self):
        return self._outer_user_no

    @outer_user_no.setter
    def outer_user_no(self, value):
        self._outer_user_no = value
    @property
    def outer_user_type(self):
        return self._outer_user_type

    @outer_user_type.setter
    def outer_user_type(self, value):
        self._outer_user_type = value
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
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.outer_user_no:
            if hasattr(self.outer_user_no, 'to_alipay_dict'):
                params['outer_user_no'] = self.outer_user_no.to_alipay_dict()
            else:
                params['outer_user_no'] = self.outer_user_no
        if self.outer_user_type:
            if hasattr(self.outer_user_type, 'to_alipay_dict'):
                params['outer_user_type'] = self.outer_user_type.to_alipay_dict()
            else:
                params['outer_user_type'] = self.outer_user_type
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
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataIntelligentdiagnosisSendModel()
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'outer_user_no' in d:
            o.outer_user_no = d['outer_user_no']
        if 'outer_user_type' in d:
            o.outer_user_type = d['outer_user_type']
        if 'question' in d:
            o.question = d['question']
        if 'question_type' in d:
            o.question_type = d['question_type']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'source_type' in d:
            o.source_type = d['source_type']
        return o


