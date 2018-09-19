#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CplifeNoticeImg(object):

    def __init__(self):
        self._image_url = None
        self._thumbnail_url = None

    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def thumbnail_url(self):
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, value):
        self._thumbnail_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.thumbnail_url:
            if hasattr(self.thumbnail_url, 'to_alipay_dict'):
                params['thumbnail_url'] = self.thumbnail_url.to_alipay_dict()
            else:
                params['thumbnail_url'] = self.thumbnail_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CplifeNoticeImg()
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'thumbnail_url' in d:
            o.thumbnail_url = d['thumbnail_url']
        return o


