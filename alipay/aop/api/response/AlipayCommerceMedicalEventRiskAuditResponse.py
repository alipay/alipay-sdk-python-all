#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalEventRiskAuditResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalEventRiskAuditResponse, self).__init__()
        self._event_id = None
        self._request_id = None
        self._risk_event_code = None
        self._risk_process = None

    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, value):
        self._event_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def risk_event_code(self):
        return self._risk_event_code

    @risk_event_code.setter
    def risk_event_code(self, value):
        self._risk_event_code = value
    @property
    def risk_process(self):
        return self._risk_process

    @risk_process.setter
    def risk_process(self, value):
        self._risk_process = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalEventRiskAuditResponse, self).parse_response_content(response_content)
        if 'event_id' in response:
            self.event_id = response['event_id']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'risk_event_code' in response:
            self.risk_event_code = response['risk_event_code']
        if 'risk_process' in response:
            self.risk_process = response['risk_process']
