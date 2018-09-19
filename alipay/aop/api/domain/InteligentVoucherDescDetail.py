#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InteligentVoucherDescDetail(object):

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
        self._details = value
    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        self._images = value
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
            if hasattr(self.details, 'to_alipay_dict'):
                params['details'] = self.details.to_alipay_dict()
            else:
                params['details'] = self.details
        if self.images:
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
        o = InteligentVoucherDescDetail()
        if 'details' in d:
            o.details = d['details']
        if 'images' in d:
            o.images = d['images']
        if 'title' in d:
            o.title = d['title']
        if 'url' in d:
            o.url = d['url']
        return o


