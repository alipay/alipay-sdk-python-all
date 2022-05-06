#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCliveSystemSendModel(object):

    def __init__(self):
        self._content = None
        self._conversation_id = None
        self._src = None
        self._visitor_id = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCliveSystemSendModel()
        if 'content' in d:
            o.content = d['content']
        if 'conversation_id' in d:
            o.conversation_id = d['conversation_id']
        if 'src' in d:
            o.src = d['src']
        if 'visitor_id' in d:
            o.visitor_id = d['visitor_id']
        return o


