#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalEventRiskAuditResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalEventRiskAuditResponse, self).__init__()
        self._audit_item_result_list = None
        self._event_id = None
        self._notarization = None
        self._request_id = None
        self._result = None
        self._risk_event_code = None
        self._risk_label_list = None
        self._risk_process = None

    @property
    def audit_item_result_list(self):
        return self._audit_item_result_list

    @audit_item_result_list.setter
    def audit_item_result_list(self, value):
        self._audit_item_result_list = value
    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, value):
        self._event_id = value
    @property
    def notarization(self):
        return self._notarization

    @notarization.setter
    def notarization(self, value):
        self._notarization = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def risk_event_code(self):
        return self._risk_event_code

    @risk_event_code.setter
    def risk_event_code(self, value):
        self._risk_event_code = value
    @property
    def risk_label_list(self):
        return self._risk_label_list

    @risk_label_list.setter
    def risk_label_list(self, value):
        self._risk_label_list = value
    @property
    def risk_process(self):
        return self._risk_process

    @risk_process.setter
    def risk_process(self, value):
        self._risk_process = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalEventRiskAuditResponse, self).parse_response_content(response_content)
        if 'audit_item_result_list' in response:
            self.audit_item_result_list = response['audit_item_result_list']
        if 'event_id' in response:
            self.event_id = response['event_id']
        if 'notarization' in response:
            self.notarization = response['notarization']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'result' in response:
            self.result = response['result']
        if 'risk_event_code' in response:
            self.risk_event_code = response['risk_event_code']
        if 'risk_label_list' in response:
            self.risk_label_list = response['risk_label_list']
        if 'risk_process' in response:
            self.risk_process = response['risk_process']
