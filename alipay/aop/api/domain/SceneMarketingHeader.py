#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SceneMarketingHeader(object):

    def __init__(self):
        self._icon = None
        self._sub_title = None
        self._summary = None
        self._tags = None
        self._title = None
        self._url = None

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value
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
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        if self.summary:
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
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
        o = SceneMarketingHeader()
        if 'icon' in d:
            o.icon = d['icon']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'summary' in d:
            o.summary = d['summary']
        if 'tags' in d:
            o.tags = d['tags']
        if 'title' in d:
            o.title = d['title']
        if 'url' in d:
            o.url = d['url']
        return o


