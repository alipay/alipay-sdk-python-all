#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MsgContent(object):

    def __init__(self):
        self._content_timestamp = None
        self._content_type = None

    @property
    def content_timestamp(self):
        return self._content_timestamp

    @content_timestamp.setter
    def content_timestamp(self, value):
        self._content_timestamp = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_timestamp:
            if hasattr(self.content_timestamp, 'to_alipay_dict'):
                params['content_timestamp'] = self.content_timestamp.to_alipay_dict()
            else:
                params['content_timestamp'] = self.content_timestamp
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MsgContent()
        if 'content_timestamp' in d:
            o.content_timestamp = d['content_timestamp']
        if 'content_type' in d:
            o.content_type = d['content_type']
        return o


