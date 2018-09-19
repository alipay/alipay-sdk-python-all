#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpusInfo(object):

    def __init__(self):
        self._display_weight = None
        self._external_opus_id = None
        self._media_id = None
        self._media_type = None
        self._media_url = None
        self._opus_id = None
        self._title = None

    @property
    def display_weight(self):
        return self._display_weight

    @display_weight.setter
    def display_weight(self, value):
        self._display_weight = value
    @property
    def external_opus_id(self):
        return self._external_opus_id

    @external_opus_id.setter
    def external_opus_id(self, value):
        self._external_opus_id = value
    @property
    def media_id(self):
        return self._media_id

    @media_id.setter
    def media_id(self, value):
        self._media_id = value
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
    @property
    def opus_id(self):
        return self._opus_id

    @opus_id.setter
    def opus_id(self, value):
        self._opus_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.display_weight:
            if hasattr(self.display_weight, 'to_alipay_dict'):
                params['display_weight'] = self.display_weight.to_alipay_dict()
            else:
                params['display_weight'] = self.display_weight
        if self.external_opus_id:
            if hasattr(self.external_opus_id, 'to_alipay_dict'):
                params['external_opus_id'] = self.external_opus_id.to_alipay_dict()
            else:
                params['external_opus_id'] = self.external_opus_id
        if self.media_id:
            if hasattr(self.media_id, 'to_alipay_dict'):
                params['media_id'] = self.media_id.to_alipay_dict()
            else:
                params['media_id'] = self.media_id
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
        if self.opus_id:
            if hasattr(self.opus_id, 'to_alipay_dict'):
                params['opus_id'] = self.opus_id.to_alipay_dict()
            else:
                params['opus_id'] = self.opus_id
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpusInfo()
        if 'display_weight' in d:
            o.display_weight = d['display_weight']
        if 'external_opus_id' in d:
            o.external_opus_id = d['external_opus_id']
        if 'media_id' in d:
            o.media_id = d['media_id']
        if 'media_type' in d:
            o.media_type = d['media_type']
        if 'media_url' in d:
            o.media_url = d['media_url']
        if 'opus_id' in d:
            o.opus_id = d['opus_id']
        if 'title' in d:
            o.title = d['title']
        return o


