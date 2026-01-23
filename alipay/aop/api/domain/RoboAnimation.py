#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RoboAnimation(object):

    def __init__(self):
        self._animation_id = None
        self._animation_url = None
        self._example_image_url = None
        self._sort = None

    @property
    def animation_id(self):
        return self._animation_id

    @animation_id.setter
    def animation_id(self, value):
        self._animation_id = value
    @property
    def animation_url(self):
        return self._animation_url

    @animation_url.setter
    def animation_url(self, value):
        self._animation_url = value
    @property
    def example_image_url(self):
        return self._example_image_url

    @example_image_url.setter
    def example_image_url(self, value):
        self._example_image_url = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value


    def to_alipay_dict(self):
        params = dict()
        if self.animation_id:
            if hasattr(self.animation_id, 'to_alipay_dict'):
                params['animation_id'] = self.animation_id.to_alipay_dict()
            else:
                params['animation_id'] = self.animation_id
        if self.animation_url:
            if hasattr(self.animation_url, 'to_alipay_dict'):
                params['animation_url'] = self.animation_url.to_alipay_dict()
            else:
                params['animation_url'] = self.animation_url
        if self.example_image_url:
            if hasattr(self.example_image_url, 'to_alipay_dict'):
                params['example_image_url'] = self.example_image_url.to_alipay_dict()
            else:
                params['example_image_url'] = self.example_image_url
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoboAnimation()
        if 'animation_id' in d:
            o.animation_id = d['animation_id']
        if 'animation_url' in d:
            o.animation_url = d['animation_url']
        if 'example_image_url' in d:
            o.example_image_url = d['example_image_url']
        if 'sort' in d:
            o.sort = d['sort']
        return o


