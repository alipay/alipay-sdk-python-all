#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAgentAuditQueryModel(object):

    def __init__(self):
        self._agent_id = None
        self._audit_id = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def audit_id(self):
        return self._audit_id

    @audit_id.setter
    def audit_id(self, value):
        self._audit_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.audit_id:
            if hasattr(self.audit_id, 'to_alipay_dict'):
                params['audit_id'] = self.audit_id.to_alipay_dict()
            else:
                params['audit_id'] = self.audit_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAgentAuditQueryModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'audit_id' in d:
            o.audit_id = d['audit_id']
        return o


