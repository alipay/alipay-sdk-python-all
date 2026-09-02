#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAgentAuditSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAgentAuditSubmitResponse, self).__init__()
        self._audit_id = None

    @property
    def audit_id(self):
        return self._audit_id

    @audit_id.setter
    def audit_id(self, value):
        self._audit_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAgentAuditSubmitResponse, self).parse_response_content(response_content)
        if 'audit_id' in response:
            self.audit_id = response['audit_id']
