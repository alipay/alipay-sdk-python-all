#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AosSearchItem(object):

    def __init__(self):
        self._biz_id = None
        self._meta = None
        self._sequence = None
        self._snippet = None
        self._text = None
        self._title = None
        self._type = None
        self._url = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def meta(self):
        return self._meta

    @meta.setter
    def meta(self, value):
        self._meta = value
    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        self._sequence = value
    @property
    def snippet(self):
        return self._snippet

    @snippet.setter
    def snippet(self, value):
        self._snippet = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.meta:
            if hasattr(self.meta, 'to_alipay_dict'):
                params['meta'] = self.meta.to_alipay_dict()
            else:
                params['meta'] = self.meta
        if self.sequence:
            if hasattr(self.sequence, 'to_alipay_dict'):
                params['sequence'] = self.sequence.to_alipay_dict()
            else:
                params['sequence'] = self.sequence
        if self.snippet:
            if hasattr(self.snippet, 'to_alipay_dict'):
                params['snippet'] = self.snippet.to_alipay_dict()
            else:
                params['snippet'] = self.snippet
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AosSearchItem()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'meta' in d:
            o.meta = d['meta']
        if 'sequence' in d:
            o.sequence = d['sequence']
        if 'snippet' in d:
            o.snippet = d['snippet']
        if 'text' in d:
            o.text = d['text']
        if 'title' in d:
            o.title = d['title']
        if 'type' in d:
            o.type = d['type']
        if 'url' in d:
            o.url = d['url']
        return o


