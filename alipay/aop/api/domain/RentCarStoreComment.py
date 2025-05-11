#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentCarStoreComment(object):

    def __init__(self):
        self._comment_content = None
        self._comment_time = None
        self._comment_type = None

    @property
    def comment_content(self):
        return self._comment_content

    @comment_content.setter
    def comment_content(self, value):
        self._comment_content = value
    @property
    def comment_time(self):
        return self._comment_time

    @comment_time.setter
    def comment_time(self, value):
        self._comment_time = value
    @property
    def comment_type(self):
        return self._comment_type

    @comment_type.setter
    def comment_type(self, value):
        self._comment_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.comment_content:
            if hasattr(self.comment_content, 'to_alipay_dict'):
                params['comment_content'] = self.comment_content.to_alipay_dict()
            else:
                params['comment_content'] = self.comment_content
        if self.comment_time:
            if hasattr(self.comment_time, 'to_alipay_dict'):
                params['comment_time'] = self.comment_time.to_alipay_dict()
            else:
                params['comment_time'] = self.comment_time
        if self.comment_type:
            if hasattr(self.comment_type, 'to_alipay_dict'):
                params['comment_type'] = self.comment_type.to_alipay_dict()
            else:
                params['comment_type'] = self.comment_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentCarStoreComment()
        if 'comment_content' in d:
            o.comment_content = d['comment_content']
        if 'comment_time' in d:
            o.comment_time = d['comment_time']
        if 'comment_type' in d:
            o.comment_type = d['comment_type']
        return o


