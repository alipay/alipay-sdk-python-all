#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandEcoNfcBindResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandEcoNfcBindResponse, self).__init__()
        self._bind_fail_reason = None
        self._bind_success = None

    @property
    def bind_fail_reason(self):
        return self._bind_fail_reason

    @bind_fail_reason.setter
    def bind_fail_reason(self, value):
        self._bind_fail_reason = value
    @property
    def bind_success(self):
        return self._bind_success

    @bind_success.setter
    def bind_success(self, value):
        self._bind_success = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandEcoNfcBindResponse, self).parse_response_content(response_content)
        if 'bind_fail_reason' in response:
            self.bind_fail_reason = response['bind_fail_reason']
        if 'bind_success' in response:
            self.bind_success = response['bind_success']
