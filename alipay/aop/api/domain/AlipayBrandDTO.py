#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBrandDTO(object):

    def __init__(self):
        self._content = None
        self._icon_url = None
        self._title = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def icon_url(self):
        return self._icon_url

    @icon_url.setter
    def icon_url(self, value):
        self._icon_url = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.icon_url:
            if hasattr(self.icon_url, 'to_alipay_dict'):
                params['icon_url'] = self.icon_url.to_alipay_dict()
            else:
                params['icon_url'] = self.icon_url
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
        o = AlipayBrandDTO()
        if 'content' in d:
            o.content = d['content']
        if 'icon_url' in d:
            o.icon_url = d['icon_url']
        if 'title' in d:
            o.title = d['title']
        return o


