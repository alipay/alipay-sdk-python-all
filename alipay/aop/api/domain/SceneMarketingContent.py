#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SceneMarketingContent(object):

    def __init__(self):
        self._category = None
        self._icon = None
        self._image = None
        self._meaning = None
        self._meaning_desc = None
        self._tags = None
        self._tips = None
        self._title = None
        self._type = None
        self._url = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
    @property
    def meaning(self):
        return self._meaning

    @meaning.setter
    def meaning(self, value):
        self._meaning = value
    @property
    def meaning_desc(self):
        return self._meaning_desc

    @meaning_desc.setter
    def meaning_desc(self, value):
        self._meaning_desc = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = list()
            for i in value:
                self._tags.append(i)
    @property
    def tips(self):
        return self._tips

    @tips.setter
    def tips(self, value):
        if isinstance(value, list):
            self._tips = list()
            for i in value:
                self._tips.append(i)
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
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.image:
            if hasattr(self.image, 'to_alipay_dict'):
                params['image'] = self.image.to_alipay_dict()
            else:
                params['image'] = self.image
        if self.meaning:
            if hasattr(self.meaning, 'to_alipay_dict'):
                params['meaning'] = self.meaning.to_alipay_dict()
            else:
                params['meaning'] = self.meaning
        if self.meaning_desc:
            if hasattr(self.meaning_desc, 'to_alipay_dict'):
                params['meaning_desc'] = self.meaning_desc.to_alipay_dict()
            else:
                params['meaning_desc'] = self.meaning_desc
        if self.tags:
            if isinstance(self.tags, list):
                for i in range(0, len(self.tags)):
                    element = self.tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tags[i] = element.to_alipay_dict()
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        if self.tips:
            if isinstance(self.tips, list):
                for i in range(0, len(self.tips)):
                    element = self.tips[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tips[i] = element.to_alipay_dict()
            if hasattr(self.tips, 'to_alipay_dict'):
                params['tips'] = self.tips.to_alipay_dict()
            else:
                params['tips'] = self.tips
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
        o = SceneMarketingContent()
        if 'category' in d:
            o.category = d['category']
        if 'icon' in d:
            o.icon = d['icon']
        if 'image' in d:
            o.image = d['image']
        if 'meaning' in d:
            o.meaning = d['meaning']
        if 'meaning_desc' in d:
            o.meaning_desc = d['meaning_desc']
        if 'tags' in d:
            o.tags = d['tags']
        if 'tips' in d:
            o.tips = d['tips']
        if 'title' in d:
            o.title = d['title']
        if 'type' in d:
            o.type = d['type']
        if 'url' in d:
            o.url = d['url']
        return o


