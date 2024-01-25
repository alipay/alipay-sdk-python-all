#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SceneData import SceneData


class AlipayEngineeringInfrastructureAnttestopsTestcaseTriggerModel(object):

    def __init__(self):
        self._creator = None
        self._env_enum = None
        self._original_system = None
        self._scene_data = None
        self._scene_id = None
        self._sofa_group = None
        self._test_case_id = None

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def env_enum(self):
        return self._env_enum

    @env_enum.setter
    def env_enum(self, value):
        self._env_enum = value
    @property
    def original_system(self):
        return self._original_system

    @original_system.setter
    def original_system(self, value):
        self._original_system = value
    @property
    def scene_data(self):
        return self._scene_data

    @scene_data.setter
    def scene_data(self, value):
        if isinstance(value, SceneData):
            self._scene_data = value
        else:
            self._scene_data = SceneData.from_alipay_dict(value)
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def sofa_group(self):
        return self._sofa_group

    @sofa_group.setter
    def sofa_group(self, value):
        self._sofa_group = value
    @property
    def test_case_id(self):
        return self._test_case_id

    @test_case_id.setter
    def test_case_id(self, value):
        self._test_case_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.env_enum:
            if hasattr(self.env_enum, 'to_alipay_dict'):
                params['env_enum'] = self.env_enum.to_alipay_dict()
            else:
                params['env_enum'] = self.env_enum
        if self.original_system:
            if hasattr(self.original_system, 'to_alipay_dict'):
                params['original_system'] = self.original_system.to_alipay_dict()
            else:
                params['original_system'] = self.original_system
        if self.scene_data:
            if hasattr(self.scene_data, 'to_alipay_dict'):
                params['scene_data'] = self.scene_data.to_alipay_dict()
            else:
                params['scene_data'] = self.scene_data
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.sofa_group:
            if hasattr(self.sofa_group, 'to_alipay_dict'):
                params['sofa_group'] = self.sofa_group.to_alipay_dict()
            else:
                params['sofa_group'] = self.sofa_group
        if self.test_case_id:
            if hasattr(self.test_case_id, 'to_alipay_dict'):
                params['test_case_id'] = self.test_case_id.to_alipay_dict()
            else:
                params['test_case_id'] = self.test_case_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEngineeringInfrastructureAnttestopsTestcaseTriggerModel()
        if 'creator' in d:
            o.creator = d['creator']
        if 'env_enum' in d:
            o.env_enum = d['env_enum']
        if 'original_system' in d:
            o.original_system = d['original_system']
        if 'scene_data' in d:
            o.scene_data = d['scene_data']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'sofa_group' in d:
            o.sofa_group = d['sofa_group']
        if 'test_case_id' in d:
            o.test_case_id = d['test_case_id']
        return o


