#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SceneDataUnit import SceneDataUnit


class SceneData(object):

    def __init__(self):
        self._execute_env = None
        self._scene_data = None
        self._scene_name = None

    @property
    def execute_env(self):
        return self._execute_env

    @execute_env.setter
    def execute_env(self, value):
        self._execute_env = value
    @property
    def scene_data(self):
        return self._scene_data

    @scene_data.setter
    def scene_data(self, value):
        if isinstance(value, list):
            self._scene_data = list()
            for i in value:
                if isinstance(i, SceneDataUnit):
                    self._scene_data.append(i)
                else:
                    self._scene_data.append(SceneDataUnit.from_alipay_dict(i))
    @property
    def scene_name(self):
        return self._scene_name

    @scene_name.setter
    def scene_name(self, value):
        self._scene_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.execute_env:
            if hasattr(self.execute_env, 'to_alipay_dict'):
                params['execute_env'] = self.execute_env.to_alipay_dict()
            else:
                params['execute_env'] = self.execute_env
        if self.scene_data:
            if isinstance(self.scene_data, list):
                for i in range(0, len(self.scene_data)):
                    element = self.scene_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scene_data[i] = element.to_alipay_dict()
            if hasattr(self.scene_data, 'to_alipay_dict'):
                params['scene_data'] = self.scene_data.to_alipay_dict()
            else:
                params['scene_data'] = self.scene_data
        if self.scene_name:
            if hasattr(self.scene_name, 'to_alipay_dict'):
                params['scene_name'] = self.scene_name.to_alipay_dict()
            else:
                params['scene_name'] = self.scene_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneData()
        if 'execute_env' in d:
            o.execute_env = d['execute_env']
        if 'scene_data' in d:
            o.scene_data = d['scene_data']
        if 'scene_name' in d:
            o.scene_name = d['scene_name']
        return o


