#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSceneprodSignConsultResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSceneprodSignConsultResponse, self).__init__()
        self._approved = None
        self._reject_reason = None
        self._trace_id = None

    @property
    def approved(self):
        return self._approved

    @approved.setter
    def approved(self, value):
        self._approved = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSceneprodSignConsultResponse, self).parse_response_content(response_content)
        if 'approved' in response:
            self.approved = response['approved']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
