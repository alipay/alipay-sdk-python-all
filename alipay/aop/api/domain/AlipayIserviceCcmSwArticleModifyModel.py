#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ArticleAttachmentInfo import ArticleAttachmentInfo
from alipay.aop.api.domain.BaseArticleInfo import BaseArticleInfo


class AlipayIserviceCcmSwArticleModifyModel(object):

    def __init__(self):
        self._attachments = None
        self._category_id = None
        self._ccs_instance_id = None
        self._content = None
        self._extend_titles = None
        self._id = None
        self._keywords = None
        self._publish_end = None
        self._publish_start = None
        self._related_articles = None
        self._scene_codes = None
        self._title = None

    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        if isinstance(value, list):
            self._attachments = list()
            for i in value:
                if isinstance(i, ArticleAttachmentInfo):
                    self._attachments.append(i)
                else:
                    self._attachments.append(ArticleAttachmentInfo.from_alipay_dict(i))
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def ccs_instance_id(self):
        return self._ccs_instance_id

    @ccs_instance_id.setter
    def ccs_instance_id(self, value):
        self._ccs_instance_id = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def extend_titles(self):
        return self._extend_titles

    @extend_titles.setter
    def extend_titles(self, value):
        if isinstance(value, list):
            self._extend_titles = list()
            for i in value:
                self._extend_titles.append(i)
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def keywords(self):
        return self._keywords

    @keywords.setter
    def keywords(self, value):
        if isinstance(value, list):
            self._keywords = list()
            for i in value:
                self._keywords.append(i)
    @property
    def publish_end(self):
        return self._publish_end

    @publish_end.setter
    def publish_end(self, value):
        self._publish_end = value
    @property
    def publish_start(self):
        return self._publish_start

    @publish_start.setter
    def publish_start(self, value):
        self._publish_start = value
    @property
    def related_articles(self):
        return self._related_articles

    @related_articles.setter
    def related_articles(self, value):
        if isinstance(value, list):
            self._related_articles = list()
            for i in value:
                if isinstance(i, BaseArticleInfo):
                    self._related_articles.append(i)
                else:
                    self._related_articles.append(BaseArticleInfo.from_alipay_dict(i))
    @property
    def scene_codes(self):
        return self._scene_codes

    @scene_codes.setter
    def scene_codes(self, value):
        if isinstance(value, list):
            self._scene_codes = list()
            for i in value:
                self._scene_codes.append(i)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachments:
            if isinstance(self.attachments, list):
                for i in range(0, len(self.attachments)):
                    element = self.attachments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachments[i] = element.to_alipay_dict()
            if hasattr(self.attachments, 'to_alipay_dict'):
                params['attachments'] = self.attachments.to_alipay_dict()
            else:
                params['attachments'] = self.attachments
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.ccs_instance_id:
            if hasattr(self.ccs_instance_id, 'to_alipay_dict'):
                params['ccs_instance_id'] = self.ccs_instance_id.to_alipay_dict()
            else:
                params['ccs_instance_id'] = self.ccs_instance_id
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.extend_titles:
            if isinstance(self.extend_titles, list):
                for i in range(0, len(self.extend_titles)):
                    element = self.extend_titles[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.extend_titles[i] = element.to_alipay_dict()
            if hasattr(self.extend_titles, 'to_alipay_dict'):
                params['extend_titles'] = self.extend_titles.to_alipay_dict()
            else:
                params['extend_titles'] = self.extend_titles
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.keywords:
            if isinstance(self.keywords, list):
                for i in range(0, len(self.keywords)):
                    element = self.keywords[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.keywords[i] = element.to_alipay_dict()
            if hasattr(self.keywords, 'to_alipay_dict'):
                params['keywords'] = self.keywords.to_alipay_dict()
            else:
                params['keywords'] = self.keywords
        if self.publish_end:
            if hasattr(self.publish_end, 'to_alipay_dict'):
                params['publish_end'] = self.publish_end.to_alipay_dict()
            else:
                params['publish_end'] = self.publish_end
        if self.publish_start:
            if hasattr(self.publish_start, 'to_alipay_dict'):
                params['publish_start'] = self.publish_start.to_alipay_dict()
            else:
                params['publish_start'] = self.publish_start
        if self.related_articles:
            if isinstance(self.related_articles, list):
                for i in range(0, len(self.related_articles)):
                    element = self.related_articles[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_articles[i] = element.to_alipay_dict()
            if hasattr(self.related_articles, 'to_alipay_dict'):
                params['related_articles'] = self.related_articles.to_alipay_dict()
            else:
                params['related_articles'] = self.related_articles
        if self.scene_codes:
            if isinstance(self.scene_codes, list):
                for i in range(0, len(self.scene_codes)):
                    element = self.scene_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scene_codes[i] = element.to_alipay_dict()
            if hasattr(self.scene_codes, 'to_alipay_dict'):
                params['scene_codes'] = self.scene_codes.to_alipay_dict()
            else:
                params['scene_codes'] = self.scene_codes
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
        o = AlipayIserviceCcmSwArticleModifyModel()
        if 'attachments' in d:
            o.attachments = d['attachments']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'ccs_instance_id' in d:
            o.ccs_instance_id = d['ccs_instance_id']
        if 'content' in d:
            o.content = d['content']
        if 'extend_titles' in d:
            o.extend_titles = d['extend_titles']
        if 'id' in d:
            o.id = d['id']
        if 'keywords' in d:
            o.keywords = d['keywords']
        if 'publish_end' in d:
            o.publish_end = d['publish_end']
        if 'publish_start' in d:
            o.publish_start = d['publish_start']
        if 'related_articles' in d:
            o.related_articles = d['related_articles']
        if 'scene_codes' in d:
            o.scene_codes = d['scene_codes']
        if 'title' in d:
            o.title = d['title']
        return o


