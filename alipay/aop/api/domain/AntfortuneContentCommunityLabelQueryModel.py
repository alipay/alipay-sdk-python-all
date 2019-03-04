#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneContentCommunityLabelQueryModel(object):

    def __init__(self):
        self._label_scene = None

    @property
    def label_scene(self):
        return self._label_scene

    @label_scene.setter
    def label_scene(self, value):
        self._label_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.label_scene:
            if hasattr(self.label_scene, 'to_alipay_dict'):
                params['label_scene'] = self.label_scene.to_alipay_dict()
            else:
                params['label_scene'] = self.label_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneContentCommunityLabelQueryModel()
        if 'label_scene' in d:
            o.label_scene = d['label_scene']
        return o


