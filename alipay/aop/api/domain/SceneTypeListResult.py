#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SceneTypeVO import SceneTypeVO


class SceneTypeListResult(object):

    def __init__(self):
        self._scene_type_list = None

    @property
    def scene_type_list(self):
        return self._scene_type_list

    @scene_type_list.setter
    def scene_type_list(self, value):
        if isinstance(value, list):
            self._scene_type_list = list()
            for i in value:
                if isinstance(i, SceneTypeVO):
                    self._scene_type_list.append(i)
                else:
                    self._scene_type_list.append(SceneTypeVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.scene_type_list:
            if isinstance(self.scene_type_list, list):
                for i in range(0, len(self.scene_type_list)):
                    element = self.scene_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scene_type_list[i] = element.to_alipay_dict()
            if hasattr(self.scene_type_list, 'to_alipay_dict'):
                params['scene_type_list'] = self.scene_type_list.to_alipay_dict()
            else:
                params['scene_type_list'] = self.scene_type_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneTypeListResult()
        if 'scene_type_list' in d:
            o.scene_type_list = d['scene_type_list']
        return o


