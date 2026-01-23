#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalServiceaiFeedbackSendModel(object):

    def __init__(self):
        self._agent_id = None
        self._answer = None
        self._chat_id = None
        self._feedback = None
        self._open_id = None
        self._out_user_id = None
        self._out_user_type = None
        self._query = None
        self._rewrite = None
        self._scene_code = None
        self._session_id = None
        self._trace_no = None

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
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def feedback(self):
        return self._feedback

    @feedback.setter
    def feedback(self, value):
        self._feedback = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def out_user_type(self):
        return self._out_user_type

    @out_user_type.setter
    def out_user_type(self, value):
        self._out_user_type = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def rewrite(self):
        return self._rewrite

    @rewrite.setter
    def rewrite(self, value):
        self._rewrite = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def trace_no(self):
        return self._trace_no

    @trace_no.setter
    def trace_no(self, value):
        self._trace_no = value


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
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
        if self.feedback:
            if hasattr(self.feedback, 'to_alipay_dict'):
                params['feedback'] = self.feedback.to_alipay_dict()
            else:
                params['feedback'] = self.feedback
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.out_user_type:
            if hasattr(self.out_user_type, 'to_alipay_dict'):
                params['out_user_type'] = self.out_user_type.to_alipay_dict()
            else:
                params['out_user_type'] = self.out_user_type
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.rewrite:
            if hasattr(self.rewrite, 'to_alipay_dict'):
                params['rewrite'] = self.rewrite.to_alipay_dict()
            else:
                params['rewrite'] = self.rewrite
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.trace_no:
            if hasattr(self.trace_no, 'to_alipay_dict'):
                params['trace_no'] = self.trace_no.to_alipay_dict()
            else:
                params['trace_no'] = self.trace_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalServiceaiFeedbackSendModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'answer' in d:
            o.answer = d['answer']
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'feedback' in d:
            o.feedback = d['feedback']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'out_user_type' in d:
            o.out_user_type = d['out_user_type']
        if 'query' in d:
            o.query = d['query']
        if 'rewrite' in d:
            o.rewrite = d['rewrite']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'trace_no' in d:
            o.trace_no = d['trace_no']
        return o


