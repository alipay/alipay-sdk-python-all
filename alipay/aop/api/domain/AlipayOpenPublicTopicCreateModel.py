#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TopicItem import TopicItem


class AlipayOpenPublicTopicCreateModel(object):

    def __init__(self):
        self._img_url = None
        self._link_type = None
        self._link_url = None
        self._sub_title = None
        self._title = None
        self._topic_items = None

    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value
    @property
    def link_type(self):
        return self._link_type

    @link_type.setter
    def link_type(self, value):
        self._link_type = value
    @property
    def link_url(self):
        return self._link_url

    @link_url.setter
    def link_url(self, value):
        self._link_url = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def topic_items(self):
        return self._topic_items

    @topic_items.setter
    def topic_items(self, value):
        if isinstance(value, list):
            self._topic_items = list()
            for i in value:
                if isinstance(i, TopicItem):
                    self._topic_items.append(i)
                else:
                    self._topic_items.append(TopicItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.img_url:
            if hasattr(self.img_url, 'to_alipay_dict'):
                params['img_url'] = self.img_url.to_alipay_dict()
            else:
                params['img_url'] = self.img_url
        if self.link_type:
            if hasattr(self.link_type, 'to_alipay_dict'):
                params['link_type'] = self.link_type.to_alipay_dict()
            else:
                params['link_type'] = self.link_type
        if self.link_url:
            if hasattr(self.link_url, 'to_alipay_dict'):
                params['link_url'] = self.link_url.to_alipay_dict()
            else:
                params['link_url'] = self.link_url
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.topic_items:
            if isinstance(self.topic_items, list):
                for i in range(0, len(self.topic_items)):
                    element = self.topic_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.topic_items[i] = element.to_alipay_dict()
            if hasattr(self.topic_items, 'to_alipay_dict'):
                params['topic_items'] = self.topic_items.to_alipay_dict()
            else:
                params['topic_items'] = self.topic_items
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicTopicCreateModel()
        if 'img_url' in d:
            o.img_url = d['img_url']
        if 'link_type' in d:
            o.link_type = d['link_type']
        if 'link_url' in d:
            o.link_url = d['link_url']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'title' in d:
            o.title = d['title']
        if 'topic_items' in d:
            o.topic_items = d['topic_items']
        return o


