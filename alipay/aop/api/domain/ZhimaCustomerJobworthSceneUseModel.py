#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SceneInfo import SceneInfo


class ZhimaCustomerJobworthSceneUseModel(object):

    def __init__(self):
        self._extra_info = None
        self._scene_type = None

    @property
    def extra_info(self):
        return self._extra_info

    @extra_info.setter
    def extra_info(self, value):
        if isinstance(value, SceneInfo):
            self._extra_info = value
        else:
            self._extra_info = SceneInfo.from_alipay_dict(value)
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.extra_info:
            if hasattr(self.extra_info, 'to_alipay_dict'):
                params['extra_info'] = self.extra_info.to_alipay_dict()
            else:
                params['extra_info'] = self.extra_info
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
        o = ZhimaCustomerJobworthSceneUseModel()
        if 'extra_info' in d:
            o.extra_info = d['extra_info']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        return o


