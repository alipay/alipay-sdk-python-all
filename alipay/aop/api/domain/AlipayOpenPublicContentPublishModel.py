#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicContentPublishModel(object):

    def __init__(self):
        self._action_url = None
        self._article_id = None
        self._content = None
        self._cover_img = None
        self._desc = None
        self._end_time = None
        self._source = None
        self._title = None

    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value
    @property
    def article_id(self):
        return self._article_id

    @article_id.setter
    def article_id(self, value):
        self._article_id = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def cover_img(self):
        return self._cover_img

    @cover_img.setter
    def cover_img(self, value):
        self._cover_img = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_url:
            if hasattr(self.action_url, 'to_alipay_dict'):
                params['action_url'] = self.action_url.to_alipay_dict()
            else:
                params['action_url'] = self.action_url
        if self.article_id:
            if hasattr(self.article_id, 'to_alipay_dict'):
                params['article_id'] = self.article_id.to_alipay_dict()
            else:
                params['article_id'] = self.article_id
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.cover_img:
            if hasattr(self.cover_img, 'to_alipay_dict'):
                params['cover_img'] = self.cover_img.to_alipay_dict()
            else:
                params['cover_img'] = self.cover_img
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicContentPublishModel()
        if 'action_url' in d:
            o.action_url = d['action_url']
        if 'article_id' in d:
            o.article_id = d['article_id']
        if 'content' in d:
            o.content = d['content']
        if 'cover_img' in d:
            o.cover_img = d['cover_img']
        if 'desc' in d:
            o.desc = d['desc']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'source' in d:
            o.source = d['source']
        if 'title' in d:
            o.title = d['title']
        return o


