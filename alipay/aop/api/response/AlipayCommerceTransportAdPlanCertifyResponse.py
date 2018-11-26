#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportAdPlanCertifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportAdPlanCertifyResponse, self).__init__()
        self._audit_result = None
        self._message = None

    @property
    def audit_result(self):
        return self._audit_result

    @audit_result.setter
    def audit_result(self, value):
        self._audit_result = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportAdPlanCertifyResponse, self).parse_response_content(response_content)
        if 'audit_result' in response:
            self.audit_result = response['audit_result']
        if 'message' in response:
            self.message = response['message']
