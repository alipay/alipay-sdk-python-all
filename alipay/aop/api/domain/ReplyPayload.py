#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReplyChatContent import ReplyChatContent


class ReplyPayload(object):

    def __init__(self):
        self._reply_content = None
        self._reply_type = None

    @property
    def reply_content(self):
        return self._reply_content

    @reply_content.setter
    def reply_content(self, value):
        if isinstance(value, ReplyChatContent):
            self._reply_content = value
        else:
            self._reply_content = ReplyChatContent.from_alipay_dict(value)
    @property
    def reply_type(self):
        return self._reply_type

    @reply_type.setter
    def reply_type(self, value):
        self._reply_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.reply_content:
            if hasattr(self.reply_content, 'to_alipay_dict'):
                params['reply_content'] = self.reply_content.to_alipay_dict()
            else:
                params['reply_content'] = self.reply_content
        if self.reply_type:
            if hasattr(self.reply_type, 'to_alipay_dict'):
                params['reply_type'] = self.reply_type.to_alipay_dict()
            else:
                params['reply_type'] = self.reply_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReplyPayload()
        if 'reply_content' in d:
            o.reply_content = d['reply_content']
        if 'reply_type' in d:
            o.reply_type = d['reply_type']
        return o


