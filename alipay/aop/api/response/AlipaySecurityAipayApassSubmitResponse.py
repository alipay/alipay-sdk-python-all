#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityAipayApassSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityAipayApassSubmitResponse, self).__init__()
        self._agent_token = None
        self._device_token = None

    @property
    def agent_token(self):
        return self._agent_token

    @agent_token.setter
    def agent_token(self, value):
        self._agent_token = value
    @property
    def device_token(self):
        return self._device_token

    @device_token.setter
    def device_token(self, value):
        self._device_token = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityAipayApassSubmitResponse, self).parse_response_content(response_content)
        if 'agent_token' in response:
            self.agent_token = response['agent_token']
        if 'device_token' in response:
            self.device_token = response['device_token']
