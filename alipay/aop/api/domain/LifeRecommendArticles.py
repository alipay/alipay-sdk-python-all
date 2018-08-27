#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LifeRecommendArticles(object):

    def __init__(self):
        self._article_id = None
        self._article_image = None
        self._article_link = None
        self._article_read_cnt = None
        self._article_source = None
        self._article_title = None

    @property
    def article_id(self):
        return self._article_id

    @article_id.setter
    def article_id(self, value):
        self._article_id = value
    @property
    def article_image(self):
        return self._article_image

    @article_image.setter
    def article_image(self, value):
        self._article_image = value
    @property
    def article_link(self):
        return self._article_link

    @article_link.setter
    def article_link(self, value):
        self._article_link = value
    @property
    def article_read_cnt(self):
        return self._article_read_cnt

    @article_read_cnt.setter
    def article_read_cnt(self, value):
        self._article_read_cnt = value
    @property
    def article_source(self):
        return self._article_source

    @article_source.setter
    def article_source(self, value):
        self._article_source = value
    @property
    def article_title(self):
        return self._article_title

    @article_title.setter
    def article_title(self, value):
        self._article_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.article_id:
            if hasattr(self.article_id, 'to_alipay_dict'):
                params['article_id'] = self.article_id.to_alipay_dict()
            else:
                params['article_id'] = self.article_id
        if self.article_image:
            if hasattr(self.article_image, 'to_alipay_dict'):
                params['article_image'] = self.article_image.to_alipay_dict()
            else:
                params['article_image'] = self.article_image
        if self.article_link:
            if hasattr(self.article_link, 'to_alipay_dict'):
                params['article_link'] = self.article_link.to_alipay_dict()
            else:
                params['article_link'] = self.article_link
        if self.article_read_cnt:
            if hasattr(self.article_read_cnt, 'to_alipay_dict'):
                params['article_read_cnt'] = self.article_read_cnt.to_alipay_dict()
            else:
                params['article_read_cnt'] = self.article_read_cnt
        if self.article_source:
            if hasattr(self.article_source, 'to_alipay_dict'):
                params['article_source'] = self.article_source.to_alipay_dict()
            else:
                params['article_source'] = self.article_source
        if self.article_title:
            if hasattr(self.article_title, 'to_alipay_dict'):
                params['article_title'] = self.article_title.to_alipay_dict()
            else:
                params['article_title'] = self.article_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LifeRecommendArticles()
        if 'article_id' in d:
            o.article_id = d['article_id']
        if 'article_image' in d:
            o.article_image = d['article_image']
        if 'article_link' in d:
            o.article_link = d['article_link']
        if 'article_read_cnt' in d:
            o.article_read_cnt = d['article_read_cnt']
        if 'article_source' in d:
            o.article_source = d['article_source']
        if 'article_title' in d:
            o.article_title = d['article_title']
        return o


