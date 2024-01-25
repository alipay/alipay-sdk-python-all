#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HotelImageLocation(object):

    def __init__(self):
        self._image_description = None
        self._size = None
        self._url = None
        self._water_mark = None

    @property
    def image_description(self):
        return self._image_description

    @image_description.setter
    def image_description(self, value):
        self._image_description = value
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
    def water_mark(self):
        return self._water_mark

    @water_mark.setter
    def water_mark(self, value):
        self._water_mark = value


    def to_alipay_dict(self):
        params = dict()
        if self.image_description:
            if hasattr(self.image_description, 'to_alipay_dict'):
                params['image_description'] = self.image_description.to_alipay_dict()
            else:
                params['image_description'] = self.image_description
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
        if self.water_mark:
            if hasattr(self.water_mark, 'to_alipay_dict'):
                params['water_mark'] = self.water_mark.to_alipay_dict()
            else:
                params['water_mark'] = self.water_mark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HotelImageLocation()
        if 'image_description' in d:
            o.image_description = d['image_description']
        if 'size' in d:
            o.size = d['size']
        if 'url' in d:
            o.url = d['url']
        if 'water_mark' in d:
            o.water_mark = d['water_mark']
        return o


