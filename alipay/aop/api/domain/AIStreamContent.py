#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AIStreamContent(object):

    def __init__(self):
        self._content_type = None
        self._has_next = None
        self._index = None
        self._inner_biz_content = None
        self._item_id = None
        self._text = None

    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def has_next(self):
        return self._has_next

    @has_next.setter
    def has_next(self, value):
        self._has_next = value
    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value
    @property
    def inner_biz_content(self):
        return self._inner_biz_content

    @inner_biz_content.setter
    def inner_biz_content(self, value):
        self._inner_biz_content = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.has_next:
            if hasattr(self.has_next, 'to_alipay_dict'):
                params['has_next'] = self.has_next.to_alipay_dict()
            else:
                params['has_next'] = self.has_next
        if self.index:
            if hasattr(self.index, 'to_alipay_dict'):
                params['index'] = self.index.to_alipay_dict()
            else:
                params['index'] = self.index
        if self.inner_biz_content:
            if hasattr(self.inner_biz_content, 'to_alipay_dict'):
                params['inner_biz_content'] = self.inner_biz_content.to_alipay_dict()
            else:
                params['inner_biz_content'] = self.inner_biz_content
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AIStreamContent()
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'has_next' in d:
            o.has_next = d['has_next']
        if 'index' in d:
            o.index = d['index']
        if 'inner_biz_content' in d:
            o.inner_biz_content = d['inner_biz_content']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'text' in d:
            o.text = d['text']
        return o


