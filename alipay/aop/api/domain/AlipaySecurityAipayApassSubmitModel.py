#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityAipayApassSubmitModel(object):

    def __init__(self):
        self._agent_auth_token = None
        self._scene = None
        self._security_token = None

    @property
    def agent_auth_token(self):
        return self._agent_auth_token

    @agent_auth_token.setter
    def agent_auth_token(self, value):
        self._agent_auth_token = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def security_token(self):
        return self._security_token

    @security_token.setter
    def security_token(self, value):
        self._security_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_auth_token:
            if hasattr(self.agent_auth_token, 'to_alipay_dict'):
                params['agent_auth_token'] = self.agent_auth_token.to_alipay_dict()
            else:
                params['agent_auth_token'] = self.agent_auth_token
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.security_token:
            if hasattr(self.security_token, 'to_alipay_dict'):
                params['security_token'] = self.security_token.to_alipay_dict()
            else:
                params['security_token'] = self.security_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityAipayApassSubmitModel()
        if 'agent_auth_token' in d:
            o.agent_auth_token = d['agent_auth_token']
        if 'scene' in d:
            o.scene = d['scene']
        if 'security_token' in d:
            o.security_token = d['security_token']
        return o


