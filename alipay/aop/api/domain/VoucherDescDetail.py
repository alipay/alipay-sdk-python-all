#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherDescDetail(object):

    def __init__(self):
        self._details = None
        self._images = None
        self._title = None
        self._url = None

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        if isinstance(value, list):
            self._details = list()
            for i in value:
                self._details.append(i)
    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        if isinstance(value, list):
            self._images = list()
            for i in value:
                self._images.append(i)
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
        if self.details:
            if isinstance(self.details, list):
                for i in range(0, len(self.details)):
                    element = self.details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.details[i] = element.to_alipay_dict()
            if hasattr(self.details, 'to_alipay_dict'):
                params['details'] = self.details.to_alipay_dict()
            else:
                params['details'] = self.details
        if self.images:
            if isinstance(self.images, list):
                for i in range(0, len(self.images)):
                    element = self.images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.images[i] = element.to_alipay_dict()
            if hasattr(self.images, 'to_alipay_dict'):
                params['images'] = self.images.to_alipay_dict()
            else:
                params['images'] = self.images
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
        o = VoucherDescDetail()
        if 'details' in d:
            o.details = d['details']
        if 'images' in d:
            o.images = d['images']
        if 'title' in d:
            o.title = d['title']
        if 'url' in d:
            o.url = d['url']
        return o


