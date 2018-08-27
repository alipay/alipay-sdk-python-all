#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarImageUploadModel(object):

    def __init__(self):
        self._img_content = None
        self._img_type = None
        self._scene_type = None

    @property
    def img_content(self):
        return self._img_content

    @img_content.setter
    def img_content(self, value):
        self._img_content = value
    @property
    def img_type(self):
        return self._img_type

    @img_type.setter
    def img_type(self, value):
        self._img_type = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.img_content:
            if hasattr(self.img_content, 'to_alipay_dict'):
                params['img_content'] = self.img_content.to_alipay_dict()
            else:
                params['img_content'] = self.img_content
        if self.img_type:
            if hasattr(self.img_type, 'to_alipay_dict'):
                params['img_type'] = self.img_type.to_alipay_dict()
            else:
                params['img_type'] = self.img_type
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarImageUploadModel()
        if 'img_content' in d:
            o.img_content = d['img_content']
        if 'img_type' in d:
            o.img_type = d['img_type']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        return o


