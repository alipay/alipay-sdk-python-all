#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandDirectAgentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandDirectAgentQueryResponse, self).__init__()
        self._pid = None
        self._reject_reason = None
        self._status = None

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
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
        response = super(AntMerchantExpandDirectAgentQueryResponse, self).parse_response_content(response_content)
        if 'pid' in response:
            self.pid = response['pid']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
        if 'status' in response:
            self.status = response['status']
