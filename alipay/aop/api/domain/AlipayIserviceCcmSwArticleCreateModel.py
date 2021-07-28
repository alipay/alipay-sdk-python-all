#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmSwArticleCreateModel(object):

    def __init__(self):
        self._category_id = None
        self._ccs_instance_id = None
        self._content = None
        self._extend_titles = None
        self._keywords = None
        self._library_id = None
        self._scene_codes = None
        self._title = None

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
    def keywords(self):
        return self._keywords

    @keywords.setter
    def keywords(self, value):
        if isinstance(value, list):
            self._keywords = list()
            for i in value:
                self._keywords.append(i)
    @property
    def library_id(self):
        return self._library_id

    @library_id.setter
    def library_id(self, value):
        self._library_id = value
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
        if self.library_id:
            if hasattr(self.library_id, 'to_alipay_dict'):
                params['library_id'] = self.library_id.to_alipay_dict()
            else:
                params['library_id'] = self.library_id
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
        o = AlipayIserviceCcmSwArticleCreateModel()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'ccs_instance_id' in d:
            o.ccs_instance_id = d['ccs_instance_id']
        if 'content' in d:
            o.content = d['content']
        if 'extend_titles' in d:
            o.extend_titles = d['extend_titles']
        if 'keywords' in d:
            o.keywords = d['keywords']
        if 'library_id' in d:
            o.library_id = d['library_id']
        if 'scene_codes' in d:
            o.scene_codes = d['scene_codes']
        if 'title' in d:
            o.title = d['title']
        return o


