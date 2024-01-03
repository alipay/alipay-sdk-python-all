#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerJobworthAuthenticationPreconsultResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerJobworthAuthenticationPreconsultResponse, self).__init__()
        self._pre_check_success = None
        self._reason = None

    @property
    def pre_check_success(self):
        return self._pre_check_success

    @pre_check_success.setter
    def pre_check_success(self, value):
        self._pre_check_success = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerJobworthAuthenticationPreconsultResponse, self).parse_response_content(response_content)
        if 'pre_check_success' in response:
            self.pre_check_success = response['pre_check_success']
        if 'reason' in response:
            self.reason = response['reason']
