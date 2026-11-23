#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VideoItem(object):

    def __init__(self):
        self._afts_id = None
        self._duration = None
        self._height = None
        self._size = None
        self._thumb_url = None
        self._video_id = None
        self._video_pattern = None
        self._video_url = None
        self._width = None

    @property
    def afts_id(self):
        return self._afts_id

    @afts_id.setter
    def afts_id(self, value):
        self._afts_id = value
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
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def thumb_url(self):
        return self._thumb_url

    @thumb_url.setter
    def thumb_url(self, value):
        self._thumb_url = value
    @property
    def video_id(self):
        return self._video_id

    @video_id.setter
    def video_id(self, value):
        self._video_id = value
    @property
    def video_pattern(self):
        return self._video_pattern

    @video_pattern.setter
    def video_pattern(self, value):
        self._video_pattern = value
    @property
    def video_url(self):
        return self._video_url

    @video_url.setter
    def video_url(self, value):
        self._video_url = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.afts_id:
            if hasattr(self.afts_id, 'to_alipay_dict'):
                params['afts_id'] = self.afts_id.to_alipay_dict()
            else:
                params['afts_id'] = self.afts_id
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
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.thumb_url:
            if hasattr(self.thumb_url, 'to_alipay_dict'):
                params['thumb_url'] = self.thumb_url.to_alipay_dict()
            else:
                params['thumb_url'] = self.thumb_url
        if self.video_id:
            if hasattr(self.video_id, 'to_alipay_dict'):
                params['video_id'] = self.video_id.to_alipay_dict()
            else:
                params['video_id'] = self.video_id
        if self.video_pattern:
            if hasattr(self.video_pattern, 'to_alipay_dict'):
                params['video_pattern'] = self.video_pattern.to_alipay_dict()
            else:
                params['video_pattern'] = self.video_pattern
        if self.video_url:
            if hasattr(self.video_url, 'to_alipay_dict'):
                params['video_url'] = self.video_url.to_alipay_dict()
            else:
                params['video_url'] = self.video_url
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
        o = VideoItem()
        if 'afts_id' in d:
            o.afts_id = d['afts_id']
        if 'duration' in d:
            o.duration = d['duration']
        if 'height' in d:
            o.height = d['height']
        if 'size' in d:
            o.size = d['size']
        if 'thumb_url' in d:
            o.thumb_url = d['thumb_url']
        if 'video_id' in d:
            o.video_id = d['video_id']
        if 'video_pattern' in d:
            o.video_pattern = d['video_pattern']
        if 'video_url' in d:
            o.video_url = d['video_url']
        if 'width' in d:
            o.width = d['width']
        return o


