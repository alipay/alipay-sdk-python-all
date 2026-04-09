#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Agentproperties import Agentproperties
from alipay.aop.api.domain.GuardrailsContent import GuardrailsContent


class AlipaySecurityRiskGuardrailsAgentDetectModel(object):

    def __init__(self):
        self._agent_code = None
        self._agent_properties = None
        self._app_code = None
        self._business_data_id = None
        self._business_name = None
        self._business_node = None
        self._business_sub_scene = None
        self._check_contents = None

    @property
    def agent_code(self):
        return self._agent_code

    @agent_code.setter
    def agent_code(self, value):
        self._agent_code = value
    @property
    def agent_properties(self):
        return self._agent_properties

    @agent_properties.setter
    def agent_properties(self, value):
        if isinstance(value, Agentproperties):
            self._agent_properties = value
        else:
            self._agent_properties = Agentproperties.from_alipay_dict(value)
    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def business_data_id(self):
        return self._business_data_id

    @business_data_id.setter
    def business_data_id(self, value):
        self._business_data_id = value
    @property
    def business_name(self):
        return self._business_name

    @business_name.setter
    def business_name(self, value):
        self._business_name = value
    @property
    def business_node(self):
        return self._business_node

    @business_node.setter
    def business_node(self, value):
        self._business_node = value
    @property
    def business_sub_scene(self):
        return self._business_sub_scene

    @business_sub_scene.setter
    def business_sub_scene(self, value):
        self._business_sub_scene = value
    @property
    def check_contents(self):
        return self._check_contents

    @check_contents.setter
    def check_contents(self, value):
        if isinstance(value, list):
            self._check_contents = list()
            for i in value:
                if isinstance(i, GuardrailsContent):
                    self._check_contents.append(i)
                else:
                    self._check_contents.append(GuardrailsContent.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.agent_code:
            if hasattr(self.agent_code, 'to_alipay_dict'):
                params['agent_code'] = self.agent_code.to_alipay_dict()
            else:
                params['agent_code'] = self.agent_code
        if self.agent_properties:
            if hasattr(self.agent_properties, 'to_alipay_dict'):
                params['agent_properties'] = self.agent_properties.to_alipay_dict()
            else:
                params['agent_properties'] = self.agent_properties
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.business_data_id:
            if hasattr(self.business_data_id, 'to_alipay_dict'):
                params['business_data_id'] = self.business_data_id.to_alipay_dict()
            else:
                params['business_data_id'] = self.business_data_id
        if self.business_name:
            if hasattr(self.business_name, 'to_alipay_dict'):
                params['business_name'] = self.business_name.to_alipay_dict()
            else:
                params['business_name'] = self.business_name
        if self.business_node:
            if hasattr(self.business_node, 'to_alipay_dict'):
                params['business_node'] = self.business_node.to_alipay_dict()
            else:
                params['business_node'] = self.business_node
        if self.business_sub_scene:
            if hasattr(self.business_sub_scene, 'to_alipay_dict'):
                params['business_sub_scene'] = self.business_sub_scene.to_alipay_dict()
            else:
                params['business_sub_scene'] = self.business_sub_scene
        if self.check_contents:
            if isinstance(self.check_contents, list):
                for i in range(0, len(self.check_contents)):
                    element = self.check_contents[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.check_contents[i] = element.to_alipay_dict()
            if hasattr(self.check_contents, 'to_alipay_dict'):
                params['check_contents'] = self.check_contents.to_alipay_dict()
            else:
                params['check_contents'] = self.check_contents
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskGuardrailsAgentDetectModel()
        if 'agent_code' in d:
            o.agent_code = d['agent_code']
        if 'agent_properties' in d:
            o.agent_properties = d['agent_properties']
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'business_data_id' in d:
            o.business_data_id = d['business_data_id']
        if 'business_name' in d:
            o.business_name = d['business_name']
        if 'business_node' in d:
            o.business_node = d['business_node']
        if 'business_sub_scene' in d:
            o.business_sub_scene = d['business_sub_scene']
        if 'check_contents' in d:
            o.check_contents = d['check_contents']
        return o


