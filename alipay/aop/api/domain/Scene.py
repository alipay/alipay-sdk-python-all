#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Scene(object):

    def __init__(self):
        self._scene_id = None

    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Scene()
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        return o


