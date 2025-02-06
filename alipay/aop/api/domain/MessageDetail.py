#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MessageDetail(object):

    def __init__(self):
        self._content = None
        self._feedback_status = None
        self._message_id = None
        self._role = None
        self._session_id = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def feedback_status(self):
        return self._feedback_status

    @feedback_status.setter
    def feedback_status(self, value):
        self._feedback_status = value
    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, value):
        self._message_id = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.feedback_status:
            if hasattr(self.feedback_status, 'to_alipay_dict'):
                params['feedback_status'] = self.feedback_status.to_alipay_dict()
            else:
                params['feedback_status'] = self.feedback_status
        if self.message_id:
            if hasattr(self.message_id, 'to_alipay_dict'):
                params['message_id'] = self.message_id.to_alipay_dict()
            else:
                params['message_id'] = self.message_id
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
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
        o = MessageDetail()
        if 'content' in d:
            o.content = d['content']
        if 'feedback_status' in d:
            o.feedback_status = d['feedback_status']
        if 'message_id' in d:
            o.message_id = d['message_id']
        if 'role' in d:
            o.role = d['role']
        if 'session_id' in d:
            o.session_id = d['session_id']
        return o


