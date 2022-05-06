#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FloorVideo(object):

    def __init__(self):
        self._floor_id = None
        self._if_changed = None
        self._video_urls = None

    @property
    def floor_id(self):
        return self._floor_id

    @floor_id.setter
    def floor_id(self, value):
        self._floor_id = value
    @property
    def if_changed(self):
        return self._if_changed

    @if_changed.setter
    def if_changed(self, value):
        self._if_changed = value
    @property
    def video_urls(self):
        return self._video_urls

    @video_urls.setter
    def video_urls(self, value):
        if isinstance(value, list):
            self._video_urls = list()
            for i in value:
                self._video_urls.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.floor_id:
            if hasattr(self.floor_id, 'to_alipay_dict'):
                params['floor_id'] = self.floor_id.to_alipay_dict()
            else:
                params['floor_id'] = self.floor_id
        if self.if_changed:
            if hasattr(self.if_changed, 'to_alipay_dict'):
                params['if_changed'] = self.if_changed.to_alipay_dict()
            else:
                params['if_changed'] = self.if_changed
        if self.video_urls:
            if isinstance(self.video_urls, list):
                for i in range(0, len(self.video_urls)):
                    element = self.video_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.video_urls[i] = element.to_alipay_dict()
            if hasattr(self.video_urls, 'to_alipay_dict'):
                params['video_urls'] = self.video_urls.to_alipay_dict()
            else:
                params['video_urls'] = self.video_urls
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FloorVideo()
        if 'floor_id' in d:
            o.floor_id = d['floor_id']
        if 'if_changed' in d:
            o.if_changed = d['if_changed']
        if 'video_urls' in d:
            o.video_urls = d['video_urls']
        return o


