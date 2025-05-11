#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenChatContent import OpenChatContent


class ReplyChatContent(object):

    def __init__(self):
        self._chat_id = None
        self._content = None
        self._content_type = None
        self._context = None
        self._role_type = None
        self._session_id = None
        self._unit_id = None

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
        if isinstance(value, OpenChatContent):
            self._content = value
        else:
            self._content = OpenChatContent.from_alipay_dict(value)
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        self._context = value
    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def unit_id(self):
        return self._unit_id

    @unit_id.setter
    def unit_id(self, value):
        self._unit_id = value


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
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.context:
            if hasattr(self.context, 'to_alipay_dict'):
                params['context'] = self.context.to_alipay_dict()
            else:
                params['context'] = self.context
        if self.role_type:
            if hasattr(self.role_type, 'to_alipay_dict'):
                params['role_type'] = self.role_type.to_alipay_dict()
            else:
                params['role_type'] = self.role_type
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.unit_id:
            if hasattr(self.unit_id, 'to_alipay_dict'):
                params['unit_id'] = self.unit_id.to_alipay_dict()
            else:
                params['unit_id'] = self.unit_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReplyChatContent()
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'content' in d:
            o.content = d['content']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'context' in d:
            o.context = d['context']
        if 'role_type' in d:
            o.role_type = d['role_type']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'unit_id' in d:
            o.unit_id = d['unit_id']
        return o


