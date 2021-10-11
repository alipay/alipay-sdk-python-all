#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCliveChatSendModel(object):

    def __init__(self):
        self._content = None
        self._content_type = None
        self._conversation_id = None
        self._src = None
        self._visitor_id = None
        self._visitor_name = None
        self._visitor_token = None
        self._visitor_type = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def conversation_id(self):
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, value):
        self._conversation_id = value
    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, value):
        self._src = value
    @property
    def visitor_id(self):
        return self._visitor_id

    @visitor_id.setter
    def visitor_id(self, value):
        self._visitor_id = value
    @property
    def visitor_name(self):
        return self._visitor_name

    @visitor_name.setter
    def visitor_name(self, value):
        self._visitor_name = value
    @property
    def visitor_token(self):
        return self._visitor_token

    @visitor_token.setter
    def visitor_token(self, value):
        self._visitor_token = value
    @property
    def visitor_type(self):
        return self._visitor_type

    @visitor_type.setter
    def visitor_type(self, value):
        self._visitor_type = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.conversation_id:
            if hasattr(self.conversation_id, 'to_alipay_dict'):
                params['conversation_id'] = self.conversation_id.to_alipay_dict()
            else:
                params['conversation_id'] = self.conversation_id
        if self.src:
            if hasattr(self.src, 'to_alipay_dict'):
                params['src'] = self.src.to_alipay_dict()
            else:
                params['src'] = self.src
        if self.visitor_id:
            if hasattr(self.visitor_id, 'to_alipay_dict'):
                params['visitor_id'] = self.visitor_id.to_alipay_dict()
            else:
                params['visitor_id'] = self.visitor_id
        if self.visitor_name:
            if hasattr(self.visitor_name, 'to_alipay_dict'):
                params['visitor_name'] = self.visitor_name.to_alipay_dict()
            else:
                params['visitor_name'] = self.visitor_name
        if self.visitor_token:
            if hasattr(self.visitor_token, 'to_alipay_dict'):
                params['visitor_token'] = self.visitor_token.to_alipay_dict()
            else:
                params['visitor_token'] = self.visitor_token
        if self.visitor_type:
            if hasattr(self.visitor_type, 'to_alipay_dict'):
                params['visitor_type'] = self.visitor_type.to_alipay_dict()
            else:
                params['visitor_type'] = self.visitor_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCliveChatSendModel()
        if 'content' in d:
            o.content = d['content']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'conversation_id' in d:
            o.conversation_id = d['conversation_id']
        if 'src' in d:
            o.src = d['src']
        if 'visitor_id' in d:
            o.visitor_id = d['visitor_id']
        if 'visitor_name' in d:
            o.visitor_name = d['visitor_name']
        if 'visitor_token' in d:
            o.visitor_token = d['visitor_token']
        if 'visitor_type' in d:
            o.visitor_type = d['visitor_type']
        return o


