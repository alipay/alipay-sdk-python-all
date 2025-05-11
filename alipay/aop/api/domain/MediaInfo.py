#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MediaInfo(object):

    def __init__(self):
        self._media_source = None
        self._media_type = None
        self._media_url = None

    @property
    def media_source(self):
        return self._media_source

    @media_source.setter
    def media_source(self, value):
        self._media_source = value
    @property
    def media_type(self):
        return self._media_type

    @media_type.setter
    def media_type(self, value):
        self._media_type = value
    @property
    def media_url(self):
        return self._media_url

    @media_url.setter
    def media_url(self, value):
        self._media_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.media_source:
            if hasattr(self.media_source, 'to_alipay_dict'):
                params['media_source'] = self.media_source.to_alipay_dict()
            else:
                params['media_source'] = self.media_source
        if self.media_type:
            if hasattr(self.media_type, 'to_alipay_dict'):
                params['media_type'] = self.media_type.to_alipay_dict()
            else:
                params['media_type'] = self.media_type
        if self.media_url:
            if hasattr(self.media_url, 'to_alipay_dict'):
                params['media_url'] = self.media_url.to_alipay_dict()
            else:
                params['media_url'] = self.media_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MediaInfo()
        if 'media_source' in d:
            o.media_source = d['media_source']
        if 'media_type' in d:
            o.media_type = d['media_type']
        if 'media_url' in d:
            o.media_url = d['media_url']
        return o


