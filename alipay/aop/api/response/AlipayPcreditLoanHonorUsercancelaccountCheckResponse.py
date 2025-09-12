#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanHonorUsercancelaccountCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanHonorUsercancelaccountCheckResponse, self).__init__()
        self._logoff_allowed = None
        self._reason = None

    @property
    def logoff_allowed(self):
        return self._logoff_allowed

    @logoff_allowed.setter
    def logoff_allowed(self, value):
        self._logoff_allowed = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanHonorUsercancelaccountCheckResponse, self).parse_response_content(response_content)
        if 'logoff_allowed' in response:
            self.logoff_allowed = response['logoff_allowed']
        if 'reason' in response:
            self.reason = response['reason']
