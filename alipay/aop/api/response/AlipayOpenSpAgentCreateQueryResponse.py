#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpAgentCreateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpAgentCreateQueryResponse, self).__init__()
        self._agent_id = None
        self._agent_name = None
        self._status = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def agent_name(self):
        return self._agent_name

    @agent_name.setter
    def agent_name(self, value):
        self._agent_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpAgentCreateQueryResponse, self).parse_response_content(response_content)
        if 'agent_id' in response:
            self.agent_id = response['agent_id']
        if 'agent_name' in response:
            self.agent_name = response['agent_name']
        if 'status' in response:
            self.status = response['status']
