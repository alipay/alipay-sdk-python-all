#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentCarTableInfo(object):

    def __init__(self):
        self._content = None
        self._great = None
        self._title = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def great(self):
        return self._great

    @great.setter
    def great(self, value):
        self._great = value
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
        if self.great:
            if hasattr(self.great, 'to_alipay_dict'):
                params['great'] = self.great.to_alipay_dict()
            else:
                params['great'] = self.great
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
        o = RentCarTableInfo()
        if 'content' in d:
            o.content = d['content']
        if 'great' in d:
            o.great = d['great']
        if 'title' in d:
            o.title = d['title']
        return o


