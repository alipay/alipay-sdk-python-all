#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskGuardrailsAgentDetectResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskGuardrailsAgentDetectResponse, self).__init__()
        self._action_code = None
        self._action_msg = None
        self._request_id = None
        self._safe = None
        self._session_action = None

    @property
    def action_code(self):
        return self._action_code

    @action_code.setter
    def action_code(self, value):
        self._action_code = value
    @property
    def action_msg(self):
        return self._action_msg

    @action_msg.setter
    def action_msg(self, value):
        self._action_msg = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def safe(self):
        return self._safe

    @safe.setter
    def safe(self, value):
        self._safe = value
    @property
    def session_action(self):
        return self._session_action

    @session_action.setter
    def session_action(self, value):
        self._session_action = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskGuardrailsAgentDetectResponse, self).parse_response_content(response_content)
        if 'action_code' in response:
            self.action_code = response['action_code']
        if 'action_msg' in response:
            self.action_msg = response['action_msg']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'safe' in response:
            self.safe = response['safe']
        if 'session_action' in response:
            self.session_action = response['session_action']
