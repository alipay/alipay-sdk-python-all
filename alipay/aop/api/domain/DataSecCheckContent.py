#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DataSecCheckContent(object):

    def __init__(self):
        self._data_id = None
        self._scene_type = None
        self._text = None
        self._urls = None

    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
    @property
    def urls(self):
        return self._urls

    @urls.setter
    def urls(self, value):
        if isinstance(value, list):
            self._urls = list()
            for i in value:
                self._urls.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        if self.urls:
            if isinstance(self.urls, list):
                for i in range(0, len(self.urls)):
                    element = self.urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.urls[i] = element.to_alipay_dict()
            if hasattr(self.urls, 'to_alipay_dict'):
                params['urls'] = self.urls.to_alipay_dict()
            else:
                params['urls'] = self.urls
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DataSecCheckContent()
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'text' in d:
            o.text = d['text']
        if 'urls' in d:
            o.urls = d['urls']
        return o


