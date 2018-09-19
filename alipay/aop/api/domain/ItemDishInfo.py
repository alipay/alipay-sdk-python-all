#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemDishInfo(object):

    def __init__(self):
        self._desc = None
        self._image_urls = None
        self._title = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def image_urls(self):
        return self._image_urls

    @image_urls.setter
    def image_urls(self, value):
        if isinstance(value, list):
            self._image_urls = list()
            for i in value:
                self._image_urls.append(i)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.image_urls:
            if isinstance(self.image_urls, list):
                for i in range(0, len(self.image_urls)):
                    element = self.image_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_urls[i] = element.to_alipay_dict()
            if hasattr(self.image_urls, 'to_alipay_dict'):
                params['image_urls'] = self.image_urls.to_alipay_dict()
            else:
                params['image_urls'] = self.image_urls
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
        o = ItemDishInfo()
        if 'desc' in d:
            o.desc = d['desc']
        if 'image_urls' in d:
            o.image_urls = d['image_urls']
        if 'title' in d:
            o.title = d['title']
        return o


