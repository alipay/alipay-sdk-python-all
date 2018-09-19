#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NewsfeedMediaLinkInfo(object):

    def __init__(self):
        self._content_id = None
        self._content_source = None
        self._content_type = None
        self._desc = None
        self._thumb = None
        self._title = None
        self._url = None

    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def content_source(self):
        return self._content_source

    @content_source.setter
    def content_source(self, value):
        self._content_source = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def thumb(self):
        return self._thumb

    @thumb.setter
    def thumb(self, value):
        self._thumb = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.content_source:
            if hasattr(self.content_source, 'to_alipay_dict'):
                params['content_source'] = self.content_source.to_alipay_dict()
            else:
                params['content_source'] = self.content_source
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.thumb:
            if hasattr(self.thumb, 'to_alipay_dict'):
                params['thumb'] = self.thumb.to_alipay_dict()
            else:
                params['thumb'] = self.thumb
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
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
        o = NewsfeedMediaLinkInfo()
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'content_source' in d:
            o.content_source = d['content_source']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'desc' in d:
            o.desc = d['desc']
        if 'thumb' in d:
            o.thumb = d['thumb']
        if 'title' in d:
            o.title = d['title']
        if 'url' in d:
            o.url = d['url']
        return o


