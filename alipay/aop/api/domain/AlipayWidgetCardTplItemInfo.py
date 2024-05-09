#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipayWidgetCardTplItemSimplifyInfo import AlipayWidgetCardTplItemSimplifyInfo


class AlipayWidgetCardTplItemInfo(object):

    def __init__(self):
        self._content = None
        self._content_fill_mode = None
        self._key = None
        self._key_list = None
        self._limit_size = None
        self._type = None
        self._url = None
        self._url_fill_mode = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def content_fill_mode(self):
        return self._content_fill_mode

    @content_fill_mode.setter
    def content_fill_mode(self, value):
        self._content_fill_mode = value
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def key_list(self):
        return self._key_list

    @key_list.setter
    def key_list(self, value):
        if isinstance(value, list):
            self._key_list = list()
            for i in value:
                if isinstance(i, AlipayWidgetCardTplItemSimplifyInfo):
                    self._key_list.append(i)
                else:
                    self._key_list.append(AlipayWidgetCardTplItemSimplifyInfo.from_alipay_dict(i))
    @property
    def limit_size(self):
        return self._limit_size

    @limit_size.setter
    def limit_size(self, value):
        self._limit_size = value
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
    @property
    def url_fill_mode(self):
        return self._url_fill_mode

    @url_fill_mode.setter
    def url_fill_mode(self, value):
        self._url_fill_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.content_fill_mode:
            if hasattr(self.content_fill_mode, 'to_alipay_dict'):
                params['content_fill_mode'] = self.content_fill_mode.to_alipay_dict()
            else:
                params['content_fill_mode'] = self.content_fill_mode
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.key_list:
            if isinstance(self.key_list, list):
                for i in range(0, len(self.key_list)):
                    element = self.key_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.key_list[i] = element.to_alipay_dict()
            if hasattr(self.key_list, 'to_alipay_dict'):
                params['key_list'] = self.key_list.to_alipay_dict()
            else:
                params['key_list'] = self.key_list
        if self.limit_size:
            if hasattr(self.limit_size, 'to_alipay_dict'):
                params['limit_size'] = self.limit_size.to_alipay_dict()
            else:
                params['limit_size'] = self.limit_size
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
        if self.url_fill_mode:
            if hasattr(self.url_fill_mode, 'to_alipay_dict'):
                params['url_fill_mode'] = self.url_fill_mode.to_alipay_dict()
            else:
                params['url_fill_mode'] = self.url_fill_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayWidgetCardTplItemInfo()
        if 'content' in d:
            o.content = d['content']
        if 'content_fill_mode' in d:
            o.content_fill_mode = d['content_fill_mode']
        if 'key' in d:
            o.key = d['key']
        if 'key_list' in d:
            o.key_list = d['key_list']
        if 'limit_size' in d:
            o.limit_size = d['limit_size']
        if 'type' in d:
            o.type = d['type']
        if 'url' in d:
            o.url = d['url']
        if 'url_fill_mode' in d:
            o.url_fill_mode = d['url_fill_mode']
        return o


