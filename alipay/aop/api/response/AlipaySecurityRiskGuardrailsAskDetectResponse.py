#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GuardrailsBiz import GuardrailsBiz


class AlipaySecurityRiskGuardrailsAskDetectResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskGuardrailsAskDetectResponse, self).__init__()
        self._action_code = None
        self._action_msg = None
        self._detect_check_labels = None
        self._request_id = None
        self._rewrite_content = None
        self._safe = None
        self._session_action = None
        self._suggestion = None

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
    def detect_check_labels(self):
        return self._detect_check_labels

    @detect_check_labels.setter
    def detect_check_labels(self, value):
        if isinstance(value, list):
            self._detect_check_labels = list()
            for i in value:
                self._detect_check_labels.append(i)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def rewrite_content(self):
        return self._rewrite_content

    @rewrite_content.setter
    def rewrite_content(self, value):
        if isinstance(value, list):
            self._rewrite_content = list()
            for i in value:
                if isinstance(i, GuardrailsBiz):
                    self._rewrite_content.append(i)
                else:
                    self._rewrite_content.append(GuardrailsBiz.from_alipay_dict(i))
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
    @property
    def suggestion(self):
        return self._suggestion

    @suggestion.setter
    def suggestion(self, value):
        self._suggestion = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskGuardrailsAskDetectResponse, self).parse_response_content(response_content)
        if 'action_code' in response:
            self.action_code = response['action_code']
        if 'action_msg' in response:
            self.action_msg = response['action_msg']
        if 'detect_check_labels' in response:
            self.detect_check_labels = response['detect_check_labels']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'rewrite_content' in response:
            self.rewrite_content = response['rewrite_content']
        if 'safe' in response:
            self.safe = response['safe']
        if 'session_action' in response:
            self.session_action = response['session_action']
        if 'suggestion' in response:
            self.suggestion = response['suggestion']
