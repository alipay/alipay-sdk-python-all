#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DTAgentChatContent import DTAgentChatContent
from alipay.aop.api.domain.DTAgentSceneParam import DTAgentSceneParam


class AnttechAiAgentChatQueryModel(object):

    def __init__(self):
        self._agent_id = None
        self._chat_contents = None
        self._heartbeat_mode = None
        self._scene_param = None
        self._session_id = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def chat_contents(self):
        return self._chat_contents

    @chat_contents.setter
    def chat_contents(self, value):
        if isinstance(value, list):
            self._chat_contents = list()
            for i in value:
                if isinstance(i, DTAgentChatContent):
                    self._chat_contents.append(i)
                else:
                    self._chat_contents.append(DTAgentChatContent.from_alipay_dict(i))
    @property
    def heartbeat_mode(self):
        return self._heartbeat_mode

    @heartbeat_mode.setter
    def heartbeat_mode(self, value):
        self._heartbeat_mode = value
    @property
    def scene_param(self):
        return self._scene_param

    @scene_param.setter
    def scene_param(self, value):
        if isinstance(value, DTAgentSceneParam):
            self._scene_param = value
        else:
            self._scene_param = DTAgentSceneParam.from_alipay_dict(value)
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
        if self.chat_contents:
            if isinstance(self.chat_contents, list):
                for i in range(0, len(self.chat_contents)):
                    element = self.chat_contents[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.chat_contents[i] = element.to_alipay_dict()
            if hasattr(self.chat_contents, 'to_alipay_dict'):
                params['chat_contents'] = self.chat_contents.to_alipay_dict()
            else:
                params['chat_contents'] = self.chat_contents
        if self.heartbeat_mode:
            if hasattr(self.heartbeat_mode, 'to_alipay_dict'):
                params['heartbeat_mode'] = self.heartbeat_mode.to_alipay_dict()
            else:
                params['heartbeat_mode'] = self.heartbeat_mode
        if self.scene_param:
            if hasattr(self.scene_param, 'to_alipay_dict'):
                params['scene_param'] = self.scene_param.to_alipay_dict()
            else:
                params['scene_param'] = self.scene_param
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
        o = AnttechAiAgentChatQueryModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'chat_contents' in d:
            o.chat_contents = d['chat_contents']
        if 'heartbeat_mode' in d:
            o.heartbeat_mode = d['heartbeat_mode']
        if 'scene_param' in d:
            o.scene_param = d['scene_param']
        if 'session_id' in d:
            o.session_id = d['session_id']
        return o


