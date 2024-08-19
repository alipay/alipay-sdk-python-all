#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalLargermodelFeedbackSetModel(object):

    def __init__(self):
        self._chat_id = None
        self._feedback = None
        self._feedback_tags = None
        self._open_id = None
        self._out_user_id = None
        self._outer_user_type = None
        self._scene_code = None
        self._session_id = None

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
    def feedback_tags(self):
        return self._feedback_tags

    @feedback_tags.setter
    def feedback_tags(self, value):
        if isinstance(value, list):
            self._feedback_tags = list()
            for i in value:
                self._feedback_tags.append(i)
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
    def outer_user_type(self):
        return self._outer_user_type

    @outer_user_type.setter
    def outer_user_type(self, value):
        self._outer_user_type = value
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


    def to_alipay_dict(self):
        params = dict()
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
        if self.feedback_tags:
            if isinstance(self.feedback_tags, list):
                for i in range(0, len(self.feedback_tags)):
                    element = self.feedback_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.feedback_tags[i] = element.to_alipay_dict()
            if hasattr(self.feedback_tags, 'to_alipay_dict'):
                params['feedback_tags'] = self.feedback_tags.to_alipay_dict()
            else:
                params['feedback_tags'] = self.feedback_tags
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
        if self.outer_user_type:
            if hasattr(self.outer_user_type, 'to_alipay_dict'):
                params['outer_user_type'] = self.outer_user_type.to_alipay_dict()
            else:
                params['outer_user_type'] = self.outer_user_type
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalLargermodelFeedbackSetModel()
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'feedback' in d:
            o.feedback = d['feedback']
        if 'feedback_tags' in d:
            o.feedback_tags = d['feedback_tags']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'outer_user_type' in d:
            o.outer_user_type = d['outer_user_type']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'session_id' in d:
            o.session_id = d['session_id']
        return o


