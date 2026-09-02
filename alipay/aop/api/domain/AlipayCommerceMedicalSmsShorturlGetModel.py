#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalSmsShorturlGetModel(object):

    def __init__(self):
        self._agent_id = None
        self._identity_id = None
        self._identity_type = None
        self._input_phone = None
        self._name = None
        self._param_info = None
        self._rule_id = None
        self._scene = None
        self._source = None
        self._sub_scene = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
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
    def input_phone(self):
        return self._input_phone

    @input_phone.setter
    def input_phone(self, value):
        self._input_phone = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
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
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def sub_scene(self):
        return self._sub_scene

    @sub_scene.setter
    def sub_scene(self, value):
        self._sub_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
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
        if self.input_phone:
            if hasattr(self.input_phone, 'to_alipay_dict'):
                params['input_phone'] = self.input_phone.to_alipay_dict()
            else:
                params['input_phone'] = self.input_phone
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
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
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'identity_id' in d:
            o.identity_id = d['identity_id']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'input_phone' in d:
            o.input_phone = d['input_phone']
        if 'name' in d:
            o.name = d['name']
        if 'param_info' in d:
            o.param_info = d['param_info']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'scene' in d:
            o.scene = d['scene']
        if 'source' in d:
            o.source = d['source']
        if 'sub_scene' in d:
            o.sub_scene = d['sub_scene']
        return o


