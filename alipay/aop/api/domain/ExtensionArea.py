#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExtensionArea(object):

    def __init__(self):
        self._goto_url = None
        self._height = None
        self._name = None
        self._type = None
        self._url = None

    @property
    def goto_url(self):
        return self._goto_url

    @goto_url.setter
    def goto_url(self, value):
        self._goto_url = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
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
        if self.goto_url:
            if hasattr(self.goto_url, 'to_alipay_dict'):
                params['goto_url'] = self.goto_url.to_alipay_dict()
            else:
                params['goto_url'] = self.goto_url
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
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
        o = ExtensionArea()
        if 'goto_url' in d:
            o.goto_url = d['goto_url']
        if 'height' in d:
            o.height = d['height']
        if 'name' in d:
            o.name = d['name']
        if 'type' in d:
            o.type = d['type']
        if 'url' in d:
            o.url = d['url']
        return o


