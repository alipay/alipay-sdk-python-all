#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudNextbuilderAgentConfigGetModel(object):

    def __init__(self):
        self._agent_id = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudNextbuilderAgentConfigGetModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        return o


