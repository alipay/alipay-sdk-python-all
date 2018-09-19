#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommentReplyOpenModel(object):

    def __init__(self):
        self._content = None
        self._operator_id = None
        self._reply_publish_time = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def reply_publish_time(self):
        return self._reply_publish_time

    @reply_publish_time.setter
    def reply_publish_time(self, value):
        self._reply_publish_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.reply_publish_time:
            if hasattr(self.reply_publish_time, 'to_alipay_dict'):
                params['reply_publish_time'] = self.reply_publish_time.to_alipay_dict()
            else:
                params['reply_publish_time'] = self.reply_publish_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommentReplyOpenModel()
        if 'content' in d:
            o.content = d['content']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'reply_publish_time' in d:
            o.reply_publish_time = d['reply_publish_time']
        return o


