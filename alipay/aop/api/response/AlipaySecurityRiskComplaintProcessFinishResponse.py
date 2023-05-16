#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskComplaintProcessFinishResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskComplaintProcessFinishResponse, self).__init__()
        self._complaint_process_success = None

    @property
    def complaint_process_success(self):
        return self._complaint_process_success

    @complaint_process_success.setter
    def complaint_process_success(self, value):
        self._complaint_process_success = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskComplaintProcessFinishResponse, self).parse_response_content(response_content)
        if 'complaint_process_success' in response:
            self.complaint_process_success = response['complaint_process_success']
