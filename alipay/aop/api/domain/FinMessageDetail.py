#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FinMessageDetail(object):

    def __init__(self):
        self._addition = None
        self._content = None
        self._message_id = None
        self._type = None

    @property
    def addition(self):
        return self._addition

    @addition.setter
    def addition(self, value):
        self._addition = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, value):
        self._message_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.addition:
            if hasattr(self.addition, 'to_alipay_dict'):
                params['addition'] = self.addition.to_alipay_dict()
            else:
                params['addition'] = self.addition
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.message_id:
            if hasattr(self.message_id, 'to_alipay_dict'):
                params['message_id'] = self.message_id.to_alipay_dict()
            else:
                params['message_id'] = self.message_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FinMessageDetail()
        if 'addition' in d:
            o.addition = d['addition']
        if 'content' in d:
            o.content = d['content']
        if 'message_id' in d:
            o.message_id = d['message_id']
        if 'type' in d:
            o.type = d['type']
        return o


