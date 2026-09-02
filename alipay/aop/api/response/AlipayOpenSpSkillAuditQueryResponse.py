#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpSkillAuditQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpSkillAuditQueryResponse, self).__init__()
        self._audit_result = None

    @property
    def audit_result(self):
        return self._audit_result

    @audit_result.setter
    def audit_result(self, value):
        self._audit_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpSkillAuditQueryResponse, self).parse_response_content(response_content)
        if 'audit_result' in response:
            self.audit_result = response['audit_result']
