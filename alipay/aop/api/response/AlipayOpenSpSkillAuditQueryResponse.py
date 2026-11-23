#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpSkillAuditQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpSkillAuditQueryResponse, self).__init__()
        self._audit_result = None
        self._reject_reason = None
        self._status = None

    @property
    def audit_result(self):
        return self._audit_result

    @audit_result.setter
    def audit_result(self, value):
        self._audit_result = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpSkillAuditQueryResponse, self).parse_response_content(response_content)
        if 'audit_result' in response:
            self.audit_result = response['audit_result']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
        if 'status' in response:
            self.status = response['status']
