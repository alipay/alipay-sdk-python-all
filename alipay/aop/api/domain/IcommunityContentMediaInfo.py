#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IcommunityContentMediaInfo(object):

    def __init__(self):
        self._cover_img_src = None
        self._media_content_height = None
        self._media_content_width = None
        self._media_src = None
        self._media_type = None

    @property
    def cover_img_src(self):
        return self._cover_img_src

    @cover_img_src.setter
    def cover_img_src(self, value):
        self._cover_img_src = value
    @property
    def media_content_height(self):
        return self._media_content_height

    @media_content_height.setter
    def media_content_height(self, value):
        self._media_content_height = value
    @property
    def media_content_width(self):
        return self._media_content_width

    @media_content_width.setter
    def media_content_width(self, value):
        self._media_content_width = value
    @property
    def media_src(self):
        return self._media_src

    @media_src.setter
    def media_src(self, value):
        self._media_src = value
    @property
    def media_type(self):
        return self._media_type

    @media_type.setter
    def media_type(self, value):
        self._media_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cover_img_src:
            if hasattr(self.cover_img_src, 'to_alipay_dict'):
                params['cover_img_src'] = self.cover_img_src.to_alipay_dict()
            else:
                params['cover_img_src'] = self.cover_img_src
        if self.media_content_height:
            if hasattr(self.media_content_height, 'to_alipay_dict'):
                params['media_content_height'] = self.media_content_height.to_alipay_dict()
            else:
                params['media_content_height'] = self.media_content_height
        if self.media_content_width:
            if hasattr(self.media_content_width, 'to_alipay_dict'):
                params['media_content_width'] = self.media_content_width.to_alipay_dict()
            else:
                params['media_content_width'] = self.media_content_width
        if self.media_src:
            if hasattr(self.media_src, 'to_alipay_dict'):
                params['media_src'] = self.media_src.to_alipay_dict()
            else:
                params['media_src'] = self.media_src
        if self.media_type:
            if hasattr(self.media_type, 'to_alipay_dict'):
                params['media_type'] = self.media_type.to_alipay_dict()
            else:
                params['media_type'] = self.media_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IcommunityContentMediaInfo()
        if 'cover_img_src' in d:
            o.cover_img_src = d['cover_img_src']
        if 'media_content_height' in d:
            o.media_content_height = d['media_content_height']
        if 'media_content_width' in d:
            o.media_content_width = d['media_content_width']
        if 'media_src' in d:
            o.media_src = d['media_src']
        if 'media_type' in d:
            o.media_type = d['media_type']
        return o


