#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAgentAuditQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAgentAuditQueryResponse, self).__init__()
        self._audit_status = None
        self._reject_reason = None

    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAgentAuditQueryResponse, self).parse_response_content(response_content)
        if 'audit_status' in response:
            self.audit_status = response['audit_status']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
