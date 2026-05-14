#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalSmsShorturlGetModel(object):

    def __init__(self):
        self._identity_id = None
        self._identity_type = None
        self._param_info = None
        self._rule_id = None
        self._scene = None
        self._sub_scene = None

    @property
    def identity_id(self):
        return self._identity_id

    @identity_id.setter
    def identity_id(self, value):
        self._identity_id = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def param_info(self):
        return self._param_info

    @param_info.setter
    def param_info(self, value):
        self._param_info = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def sub_scene(self):
        return self._sub_scene

    @sub_scene.setter
    def sub_scene(self, value):
        self._sub_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.identity_id:
            if hasattr(self.identity_id, 'to_alipay_dict'):
                params['identity_id'] = self.identity_id.to_alipay_dict()
            else:
                params['identity_id'] = self.identity_id
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.param_info:
            if hasattr(self.param_info, 'to_alipay_dict'):
                params['param_info'] = self.param_info.to_alipay_dict()
            else:
                params['param_info'] = self.param_info
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.sub_scene:
            if hasattr(self.sub_scene, 'to_alipay_dict'):
                params['sub_scene'] = self.sub_scene.to_alipay_dict()
            else:
                params['sub_scene'] = self.sub_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalSmsShorturlGetModel()
        if 'identity_id' in d:
            o.identity_id = d['identity_id']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'param_info' in d:
            o.param_info = d['param_info']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'scene' in d:
            o.scene = d['scene']
        if 'sub_scene' in d:
            o.sub_scene = d['sub_scene']
        return o


