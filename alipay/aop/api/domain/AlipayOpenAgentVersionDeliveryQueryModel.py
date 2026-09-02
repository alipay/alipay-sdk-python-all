#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAgentVersionDeliveryQueryModel(object):

    def __init__(self):
        self._agent_id = None
        self._agent_version = None
        self._channel = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def agent_version(self):
        return self._agent_version

    @agent_version.setter
    def agent_version(self, value):
        self._agent_version = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.agent_version:
            if hasattr(self.agent_version, 'to_alipay_dict'):
                params['agent_version'] = self.agent_version.to_alipay_dict()
            else:
                params['agent_version'] = self.agent_version
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAgentVersionDeliveryQueryModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'agent_version' in d:
            o.agent_version = d['agent_version']
        if 'channel' in d:
            o.channel = d['channel']
        return o


