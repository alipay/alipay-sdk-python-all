#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudNextbuilderAgentCompletionGenerateModel(object):

    def __init__(self):
        self._agent_id = None
        self._inputs = None
        self._outer_user_id = None
        self._request_id = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def inputs(self):
        return self._inputs

    @inputs.setter
    def inputs(self, value):
        self._inputs = value
    @property
    def outer_user_id(self):
        return self._outer_user_id

    @outer_user_id.setter
    def outer_user_id(self, value):
        self._outer_user_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.inputs:
            if hasattr(self.inputs, 'to_alipay_dict'):
                params['inputs'] = self.inputs.to_alipay_dict()
            else:
                params['inputs'] = self.inputs
        if self.outer_user_id:
            if hasattr(self.outer_user_id, 'to_alipay_dict'):
                params['outer_user_id'] = self.outer_user_id.to_alipay_dict()
            else:
                params['outer_user_id'] = self.outer_user_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudNextbuilderAgentCompletionGenerateModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'inputs' in d:
            o.inputs = d['inputs']
        if 'outer_user_id' in d:
            o.outer_user_id = d['outer_user_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


