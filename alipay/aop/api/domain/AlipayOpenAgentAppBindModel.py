#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAgentAppBindModel(object):

    def __init__(self):
        self._agent_id = None
        self._app_agentcode = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def app_agentcode(self):
        return self._app_agentcode

    @app_agentcode.setter
    def app_agentcode(self, value):
        self._app_agentcode = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.app_agentcode:
            if hasattr(self.app_agentcode, 'to_alipay_dict'):
                params['app_agentcode'] = self.app_agentcode.to_alipay_dict()
            else:
                params['app_agentcode'] = self.app_agentcode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAgentAppBindModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'app_agentcode' in d:
            o.app_agentcode = d['app_agentcode']
        return o


