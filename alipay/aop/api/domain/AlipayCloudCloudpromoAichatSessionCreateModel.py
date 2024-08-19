#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QueryAIChatSessionConfigRequest import QueryAIChatSessionConfigRequest


class AlipayCloudCloudpromoAichatSessionCreateModel(object):

    def __init__(self):
        self._agent_custom_content = None
        self._customer_id = None
        self._query_config = None
        self._scene_id = None
        self._session_id = None
        self._source_id = None

    @property
    def agent_custom_content(self):
        return self._agent_custom_content

    @agent_custom_content.setter
    def agent_custom_content(self, value):
        self._agent_custom_content = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def query_config(self):
        return self._query_config

    @query_config.setter
    def query_config(self, value):
        if isinstance(value, QueryAIChatSessionConfigRequest):
            self._query_config = value
        else:
            self._query_config = QueryAIChatSessionConfigRequest.from_alipay_dict(value)
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_custom_content:
            if hasattr(self.agent_custom_content, 'to_alipay_dict'):
                params['agent_custom_content'] = self.agent_custom_content.to_alipay_dict()
            else:
                params['agent_custom_content'] = self.agent_custom_content
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.query_config:
            if hasattr(self.query_config, 'to_alipay_dict'):
                params['query_config'] = self.query_config.to_alipay_dict()
            else:
                params['query_config'] = self.query_config
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoAichatSessionCreateModel()
        if 'agent_custom_content' in d:
            o.agent_custom_content = d['agent_custom_content']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'query_config' in d:
            o.query_config = d['query_config']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'source_id' in d:
            o.source_id = d['source_id']
        return o


