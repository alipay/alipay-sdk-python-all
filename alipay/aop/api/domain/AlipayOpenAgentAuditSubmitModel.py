#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAgentAuditSubmitModel(object):

    def __init__(self):
        self._agent_desc = None
        self._agent_id = None
        self._agent_logo = None
        self._agent_name = None

    @property
    def agent_desc(self):
        return self._agent_desc

    @agent_desc.setter
    def agent_desc(self, value):
        self._agent_desc = value
    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def agent_logo(self):
        return self._agent_logo

    @agent_logo.setter
    def agent_logo(self, value):
        self._agent_logo = value
    @property
    def agent_name(self):
        return self._agent_name

    @agent_name.setter
    def agent_name(self, value):
        self._agent_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_desc:
            if hasattr(self.agent_desc, 'to_alipay_dict'):
                params['agent_desc'] = self.agent_desc.to_alipay_dict()
            else:
                params['agent_desc'] = self.agent_desc
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.agent_logo:
            if hasattr(self.agent_logo, 'to_alipay_dict'):
                params['agent_logo'] = self.agent_logo.to_alipay_dict()
            else:
                params['agent_logo'] = self.agent_logo
        if self.agent_name:
            if hasattr(self.agent_name, 'to_alipay_dict'):
                params['agent_name'] = self.agent_name.to_alipay_dict()
            else:
                params['agent_name'] = self.agent_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAgentAuditSubmitModel()
        if 'agent_desc' in d:
            o.agent_desc = d['agent_desc']
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'agent_logo' in d:
            o.agent_logo = d['agent_logo']
        if 'agent_name' in d:
            o.agent_name = d['agent_name']
        return o


