#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UrlInfoList(object):

    def __init__(self):
        self._ai = None
        self._collect_type = None
        self._icon = None
        self._subtitle = None
        self._title = None
        self._url = None

    @property
    def ai(self):
        return self._ai

    @ai.setter
    def ai(self, value):
        self._ai = value
    @property
    def collect_type(self):
        return self._collect_type

    @collect_type.setter
    def collect_type(self, value):
        self._collect_type = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def subtitle(self):
        return self._subtitle

    @subtitle.setter
    def subtitle(self, value):
        self._subtitle = value
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
        if self.ai:
            if hasattr(self.ai, 'to_alipay_dict'):
                params['ai'] = self.ai.to_alipay_dict()
            else:
                params['ai'] = self.ai
        if self.collect_type:
            if hasattr(self.collect_type, 'to_alipay_dict'):
                params['collect_type'] = self.collect_type.to_alipay_dict()
            else:
                params['collect_type'] = self.collect_type
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.subtitle:
            if hasattr(self.subtitle, 'to_alipay_dict'):
                params['subtitle'] = self.subtitle.to_alipay_dict()
            else:
                params['subtitle'] = self.subtitle
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
        o = UrlInfoList()
        if 'ai' in d:
            o.ai = d['ai']
        if 'collect_type' in d:
            o.collect_type = d['collect_type']
        if 'icon' in d:
            o.icon = d['icon']
        if 'subtitle' in d:
            o.subtitle = d['subtitle']
        if 'title' in d:
            o.title = d['title']
        if 'url' in d:
            o.url = d['url']
        return o


