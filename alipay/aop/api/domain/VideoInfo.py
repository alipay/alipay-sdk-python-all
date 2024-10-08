#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VideoInfo(object):

    def __init__(self):
        self._duration = None
        self._height = None
        self._origin_url = None
        self._oss_url = None
        self._poster_url = None
        self._signature = None
        self._size = None
        self._url = None
        self._width = None

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def origin_url(self):
        return self._origin_url

    @origin_url.setter
    def origin_url(self, value):
        self._origin_url = value
    @property
    def oss_url(self):
        return self._oss_url

    @oss_url.setter
    def oss_url(self, value):
        self._oss_url = value
    @property
    def poster_url(self):
        return self._poster_url

    @poster_url.setter
    def poster_url(self, value):
        self._poster_url = value
    @property
    def signature(self):
        return self._signature

    @signature.setter
    def signature(self, value):
        self._signature = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.origin_url:
            if hasattr(self.origin_url, 'to_alipay_dict'):
                params['origin_url'] = self.origin_url.to_alipay_dict()
            else:
                params['origin_url'] = self.origin_url
        if self.oss_url:
            if hasattr(self.oss_url, 'to_alipay_dict'):
                params['oss_url'] = self.oss_url.to_alipay_dict()
            else:
                params['oss_url'] = self.oss_url
        if self.poster_url:
            if hasattr(self.poster_url, 'to_alipay_dict'):
                params['poster_url'] = self.poster_url.to_alipay_dict()
            else:
                params['poster_url'] = self.poster_url
        if self.signature:
            if hasattr(self.signature, 'to_alipay_dict'):
                params['signature'] = self.signature.to_alipay_dict()
            else:
                params['signature'] = self.signature
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        if self.width:
            if hasattr(self.width, 'to_alipay_dict'):
                params['width'] = self.width.to_alipay_dict()
            else:
                params['width'] = self.width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VideoInfo()
        if 'duration' in d:
            o.duration = d['duration']
        if 'height' in d:
            o.height = d['height']
        if 'origin_url' in d:
            o.origin_url = d['origin_url']
        if 'oss_url' in d:
            o.oss_url = d['oss_url']
        if 'poster_url' in d:
            o.poster_url = d['poster_url']
        if 'signature' in d:
            o.signature = d['signature']
        if 'size' in d:
            o.size = d['size']
        if 'url' in d:
            o.url = d['url']
        if 'width' in d:
            o.width = d['width']
        return o


