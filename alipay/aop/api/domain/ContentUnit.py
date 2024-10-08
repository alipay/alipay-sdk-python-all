#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StreamContent import StreamContent


class ContentUnit(object):

    def __init__(self):
        self._content = None
        self._content_id = None
        self._content_type = None
        self._index_id = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, StreamContent):
            self._content = value
        else:
            self._content = StreamContent.from_alipay_dict(value)
    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def index_id(self):
        return self._index_id

    @index_id.setter
    def index_id(self, value):
        self._index_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.index_id:
            if hasattr(self.index_id, 'to_alipay_dict'):
                params['index_id'] = self.index_id.to_alipay_dict()
            else:
                params['index_id'] = self.index_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentUnit()
        if 'content' in d:
            o.content = d['content']
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'index_id' in d:
            o.index_id = d['index_id']
        return o


