#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VideoData(object):

    def __init__(self):
        self._duration = None
        self._index = None
        self._video_id = None
        self._video_name = None
        self._video_url = None

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value
    @property
    def video_id(self):
        return self._video_id

    @video_id.setter
    def video_id(self, value):
        self._video_id = value
    @property
    def video_name(self):
        return self._video_name

    @video_name.setter
    def video_name(self, value):
        self._video_name = value
    @property
    def video_url(self):
        return self._video_url

    @video_url.setter
    def video_url(self, value):
        self._video_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.index:
            if hasattr(self.index, 'to_alipay_dict'):
                params['index'] = self.index.to_alipay_dict()
            else:
                params['index'] = self.index
        if self.video_id:
            if hasattr(self.video_id, 'to_alipay_dict'):
                params['video_id'] = self.video_id.to_alipay_dict()
            else:
                params['video_id'] = self.video_id
        if self.video_name:
            if hasattr(self.video_name, 'to_alipay_dict'):
                params['video_name'] = self.video_name.to_alipay_dict()
            else:
                params['video_name'] = self.video_name
        if self.video_url:
            if hasattr(self.video_url, 'to_alipay_dict'):
                params['video_url'] = self.video_url.to_alipay_dict()
            else:
                params['video_url'] = self.video_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VideoData()
        if 'duration' in d:
            o.duration = d['duration']
        if 'index' in d:
            o.index = d['index']
        if 'video_id' in d:
            o.video_id = d['video_id']
        if 'video_name' in d:
            o.video_name = d['video_name']
        if 'video_url' in d:
            o.video_url = d['video_url']
        return o


