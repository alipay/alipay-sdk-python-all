#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SceneDetail(object):

    def __init__(self):
        self._desc = None
        self._scene_id = None
        self._scene_image = None
        self._title = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def scene_image(self):
        return self._scene_image

    @scene_image.setter
    def scene_image(self, value):
        self._scene_image = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.scene_image:
            if hasattr(self.scene_image, 'to_alipay_dict'):
                params['scene_image'] = self.scene_image.to_alipay_dict()
            else:
                params['scene_image'] = self.scene_image
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
        o = SceneDetail()
        if 'desc' in d:
            o.desc = d['desc']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'scene_image' in d:
            o.scene_image = d['scene_image']
        if 'title' in d:
            o.title = d['title']
        return o


