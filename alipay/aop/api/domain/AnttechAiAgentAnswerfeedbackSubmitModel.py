#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechAiAgentAnswerfeedbackSubmitModel(object):

    def __init__(self):
        self._feedback = None
        self._msg_id = None
        self._scene_user_id = None
        self._session_id = None

    @property
    def feedback(self):
        return self._feedback

    @feedback.setter
    def feedback(self, value):
        self._feedback = value
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def scene_user_id(self):
        return self._scene_user_id

    @scene_user_id.setter
    def scene_user_id(self, value):
        self._scene_user_id = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.feedback:
            if hasattr(self.feedback, 'to_alipay_dict'):
                params['feedback'] = self.feedback.to_alipay_dict()
            else:
                params['feedback'] = self.feedback
        if self.msg_id:
            if hasattr(self.msg_id, 'to_alipay_dict'):
                params['msg_id'] = self.msg_id.to_alipay_dict()
            else:
                params['msg_id'] = self.msg_id
        if self.scene_user_id:
            if hasattr(self.scene_user_id, 'to_alipay_dict'):
                params['scene_user_id'] = self.scene_user_id.to_alipay_dict()
            else:
                params['scene_user_id'] = self.scene_user_id
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
        o = AnttechAiAgentAnswerfeedbackSubmitModel()
        if 'feedback' in d:
            o.feedback = d['feedback']
        if 'msg_id' in d:
            o.msg_id = d['msg_id']
        if 'scene_user_id' in d:
            o.scene_user_id = d['scene_user_id']
        if 'session_id' in d:
            o.session_id = d['session_id']
        return o


