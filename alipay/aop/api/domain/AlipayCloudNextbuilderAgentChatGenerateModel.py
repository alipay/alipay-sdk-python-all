#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudNextbuilderAgentChatGenerateModel(object):

    def __init__(self):
        self._agent_id = None
        self._inputs = None
        self._outer_user_id = None
        self._query = None
        self._request_id = None
        self._session_id = None

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
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value


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
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudNextbuilderAgentChatGenerateModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'inputs' in d:
            o.inputs = d['inputs']
        if 'outer_user_id' in d:
            o.outer_user_id = d['outer_user_id']
        if 'query' in d:
            o.query = d['query']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'session_id' in d:
            o.session_id = d['session_id']
        return o


