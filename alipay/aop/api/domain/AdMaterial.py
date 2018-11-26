#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdMaterial(object):

    def __init__(self):
        self._height = None
        self._index = None
        self._material_type = None
        self._mt_signature = None
        self._play_time = None
        self._url = None
        self._width = None

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value
    @property
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, value):
        self._material_type = value
    @property
    def mt_signature(self):
        return self._mt_signature

    @mt_signature.setter
    def mt_signature(self, value):
        self._mt_signature = value
    @property
    def play_time(self):
        return self._play_time

    @play_time.setter
    def play_time(self, value):
        self._play_time = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
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
        if self.index:
            if hasattr(self.index, 'to_alipay_dict'):
                params['index'] = self.index.to_alipay_dict()
            else:
                params['index'] = self.index
        if self.material_type:
            if hasattr(self.material_type, 'to_alipay_dict'):
                params['material_type'] = self.material_type.to_alipay_dict()
            else:
                params['material_type'] = self.material_type
        if self.mt_signature:
            if hasattr(self.mt_signature, 'to_alipay_dict'):
                params['mt_signature'] = self.mt_signature.to_alipay_dict()
            else:
                params['mt_signature'] = self.mt_signature
        if self.play_time:
            if hasattr(self.play_time, 'to_alipay_dict'):
                params['play_time'] = self.play_time.to_alipay_dict()
            else:
                params['play_time'] = self.play_time
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
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
        o = AdMaterial()
        if 'height' in d:
            o.height = d['height']
        if 'index' in d:
            o.index = d['index']
        if 'material_type' in d:
            o.material_type = d['material_type']
        if 'mt_signature' in d:
            o.mt_signature = d['mt_signature']
        if 'play_time' in d:
            o.play_time = d['play_time']
        if 'url' in d:
            o.url = d['url']
        if 'width' in d:
            o.width = d['width']
        return o


