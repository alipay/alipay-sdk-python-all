#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskGuardrailsAnswerDetectResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskGuardrailsAnswerDetectResponse, self).__init__()
        self._detect_check_labels = None
        self._request_id = None
        self._suggestion = None

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
    def suggestion(self):
        return self._suggestion

    @suggestion.setter
    def suggestion(self, value):
        self._suggestion = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskGuardrailsAnswerDetectResponse, self).parse_response_content(response_content)
        if 'detect_check_labels' in response:
            self.detect_check_labels = response['detect_check_labels']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'suggestion' in response:
            self.suggestion = response['suggestion']
