#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PhotoInfo(object):

    def __init__(self):
        self._img_height = None
        self._img_width = None
        self._name = None
        self._photo_size = None
        self._photo_url = None

    @property
    def img_height(self):
        return self._img_height

    @img_height.setter
    def img_height(self, value):
        self._img_height = value
    @property
    def img_width(self):
        return self._img_width

    @img_width.setter
    def img_width(self, value):
        self._img_width = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def photo_size(self):
        return self._photo_size

    @photo_size.setter
    def photo_size(self, value):
        self._photo_size = value
    @property
    def photo_url(self):
        return self._photo_url

    @photo_url.setter
    def photo_url(self, value):
        self._photo_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.img_height:
            if hasattr(self.img_height, 'to_alipay_dict'):
                params['img_height'] = self.img_height.to_alipay_dict()
            else:
                params['img_height'] = self.img_height
        if self.img_width:
            if hasattr(self.img_width, 'to_alipay_dict'):
                params['img_width'] = self.img_width.to_alipay_dict()
            else:
                params['img_width'] = self.img_width
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.photo_size:
            if hasattr(self.photo_size, 'to_alipay_dict'):
                params['photo_size'] = self.photo_size.to_alipay_dict()
            else:
                params['photo_size'] = self.photo_size
        if self.photo_url:
            if hasattr(self.photo_url, 'to_alipay_dict'):
                params['photo_url'] = self.photo_url.to_alipay_dict()
            else:
                params['photo_url'] = self.photo_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PhotoInfo()
        if 'img_height' in d:
            o.img_height = d['img_height']
        if 'img_width' in d:
            o.img_width = d['img_width']
        if 'name' in d:
            o.name = d['name']
        if 'photo_size' in d:
            o.photo_size = d['photo_size']
        if 'photo_url' in d:
            o.photo_url = d['photo_url']
        return o


