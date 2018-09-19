#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SceneContent(object):

    def __init__(self):
        self._article_classify = None
        self._author = None
        self._content_id = None
        self._cover = None
        self._image_list = None
        self._public_id = None
        self._public_name = None
        self._scheme = None
        self._scm = None
        self._summary = None
        self._title = None
        self._total_praise_count = None
        self._total_reply_count = None
        self._total_view_count = None
        self._type = None

    @property
    def article_classify(self):
        return self._article_classify

    @article_classify.setter
    def article_classify(self, value):
        self._article_classify = value
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value
    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def cover(self):
        return self._cover

    @cover.setter
    def cover(self, value):
        self._cover = value
    @property
    def image_list(self):
        return self._image_list

    @image_list.setter
    def image_list(self, value):
        if isinstance(value, list):
            self._image_list = list()
            for i in value:
                self._image_list.append(i)
    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value
    @property
    def public_name(self):
        return self._public_name

    @public_name.setter
    def public_name(self, value):
        self._public_name = value
    @property
    def scheme(self):
        return self._scheme

    @scheme.setter
    def scheme(self, value):
        self._scheme = value
    @property
    def scm(self):
        return self._scm

    @scm.setter
    def scm(self, value):
        self._scm = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def total_praise_count(self):
        return self._total_praise_count

    @total_praise_count.setter
    def total_praise_count(self, value):
        self._total_praise_count = value
    @property
    def total_reply_count(self):
        return self._total_reply_count

    @total_reply_count.setter
    def total_reply_count(self, value):
        self._total_reply_count = value
    @property
    def total_view_count(self):
        return self._total_view_count

    @total_view_count.setter
    def total_view_count(self, value):
        self._total_view_count = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.article_classify:
            if hasattr(self.article_classify, 'to_alipay_dict'):
                params['article_classify'] = self.article_classify.to_alipay_dict()
            else:
                params['article_classify'] = self.article_classify
        if self.author:
            if hasattr(self.author, 'to_alipay_dict'):
                params['author'] = self.author.to_alipay_dict()
            else:
                params['author'] = self.author
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.cover:
            if hasattr(self.cover, 'to_alipay_dict'):
                params['cover'] = self.cover.to_alipay_dict()
            else:
                params['cover'] = self.cover
        if self.image_list:
            if isinstance(self.image_list, list):
                for i in range(0, len(self.image_list)):
                    element = self.image_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_list[i] = element.to_alipay_dict()
            if hasattr(self.image_list, 'to_alipay_dict'):
                params['image_list'] = self.image_list.to_alipay_dict()
            else:
                params['image_list'] = self.image_list
        if self.public_id:
            if hasattr(self.public_id, 'to_alipay_dict'):
                params['public_id'] = self.public_id.to_alipay_dict()
            else:
                params['public_id'] = self.public_id
        if self.public_name:
            if hasattr(self.public_name, 'to_alipay_dict'):
                params['public_name'] = self.public_name.to_alipay_dict()
            else:
                params['public_name'] = self.public_name
        if self.scheme:
            if hasattr(self.scheme, 'to_alipay_dict'):
                params['scheme'] = self.scheme.to_alipay_dict()
            else:
                params['scheme'] = self.scheme
        if self.scm:
            if hasattr(self.scm, 'to_alipay_dict'):
                params['scm'] = self.scm.to_alipay_dict()
            else:
                params['scm'] = self.scm
        if self.summary:
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.total_praise_count:
            if hasattr(self.total_praise_count, 'to_alipay_dict'):
                params['total_praise_count'] = self.total_praise_count.to_alipay_dict()
            else:
                params['total_praise_count'] = self.total_praise_count
        if self.total_reply_count:
            if hasattr(self.total_reply_count, 'to_alipay_dict'):
                params['total_reply_count'] = self.total_reply_count.to_alipay_dict()
            else:
                params['total_reply_count'] = self.total_reply_count
        if self.total_view_count:
            if hasattr(self.total_view_count, 'to_alipay_dict'):
                params['total_view_count'] = self.total_view_count.to_alipay_dict()
            else:
                params['total_view_count'] = self.total_view_count
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneContent()
        if 'article_classify' in d:
            o.article_classify = d['article_classify']
        if 'author' in d:
            o.author = d['author']
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'cover' in d:
            o.cover = d['cover']
        if 'image_list' in d:
            o.image_list = d['image_list']
        if 'public_id' in d:
            o.public_id = d['public_id']
        if 'public_name' in d:
            o.public_name = d['public_name']
        if 'scheme' in d:
            o.scheme = d['scheme']
        if 'scm' in d:
            o.scm = d['scm']
        if 'summary' in d:
            o.summary = d['summary']
        if 'title' in d:
            o.title = d['title']
        if 'total_praise_count' in d:
            o.total_praise_count = d['total_praise_count']
        if 'total_reply_count' in d:
            o.total_reply_count = d['total_reply_count']
        if 'total_view_count' in d:
            o.total_view_count = d['total_view_count']
        if 'type' in d:
            o.type = d['type']
        return o


