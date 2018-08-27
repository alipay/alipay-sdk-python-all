#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NewsfeedMediaVideoInfo(object):

    def __init__(self):
        self._height = None
        self._img_id = None
        self._video_id = None
        self._width = None

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def img_id(self):
        return self._img_id

    @img_id.setter
    def img_id(self, value):
        self._img_id = value
    @property
    def video_id(self):
        return self._video_id

    @video_id.setter
    def video_id(self, value):
        self._video_id = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.img_id:
            if hasattr(self.img_id, 'to_alipay_dict'):
                params['img_id'] = self.img_id.to_alipay_dict()
            else:
                params['img_id'] = self.img_id
        if self.video_id:
            if hasattr(self.video_id, 'to_alipay_dict'):
                params['video_id'] = self.video_id.to_alipay_dict()
            else:
                params['video_id'] = self.video_id
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
        o = NewsfeedMediaVideoInfo()
        if 'height' in d:
            o.height = d['height']
        if 'img_id' in d:
            o.img_id = d['img_id']
        if 'video_id' in d:
            o.video_id = d['video_id']
        if 'width' in d:
            o.width = d['width']
        return o


