#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PoapInfoDTO(object):

    def __init__(self):
        self._medal_id = None
        self._medal_meta_id = None
        self._name = None
        self._thumbnail_url = None

    @property
    def medal_id(self):
        return self._medal_id

    @medal_id.setter
    def medal_id(self, value):
        self._medal_id = value
    @property
    def medal_meta_id(self):
        return self._medal_meta_id

    @medal_meta_id.setter
    def medal_meta_id(self, value):
        self._medal_meta_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def thumbnail_url(self):
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, value):
        self._thumbnail_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.medal_id:
            if hasattr(self.medal_id, 'to_alipay_dict'):
                params['medal_id'] = self.medal_id.to_alipay_dict()
            else:
                params['medal_id'] = self.medal_id
        if self.medal_meta_id:
            if hasattr(self.medal_meta_id, 'to_alipay_dict'):
                params['medal_meta_id'] = self.medal_meta_id.to_alipay_dict()
            else:
                params['medal_meta_id'] = self.medal_meta_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
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
        o = PoapInfoDTO()
        if 'medal_id' in d:
            o.medal_id = d['medal_id']
        if 'medal_meta_id' in d:
            o.medal_meta_id = d['medal_meta_id']
        if 'name' in d:
            o.name = d['name']
        if 'thumbnail_url' in d:
            o.thumbnail_url = d['thumbnail_url']
        return o


