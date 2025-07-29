#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VideoValueRequest(object):

    def __init__(self):
        self._video_id = None
        self._video_name = None
        self._video_size = None
        self._video_type = None

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
    def video_size(self):
        return self._video_size

    @video_size.setter
    def video_size(self, value):
        self._video_size = value
    @property
    def video_type(self):
        return self._video_type

    @video_type.setter
    def video_type(self, value):
        self._video_type = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.video_size:
            if hasattr(self.video_size, 'to_alipay_dict'):
                params['video_size'] = self.video_size.to_alipay_dict()
            else:
                params['video_size'] = self.video_size
        if self.video_type:
            if hasattr(self.video_type, 'to_alipay_dict'):
                params['video_type'] = self.video_type.to_alipay_dict()
            else:
                params['video_type'] = self.video_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VideoValueRequest()
        if 'video_id' in d:
            o.video_id = d['video_id']
        if 'video_name' in d:
            o.video_name = d['video_name']
        if 'video_size' in d:
            o.video_size = d['video_size']
        if 'video_type' in d:
            o.video_type = d['video_type']
        return o


