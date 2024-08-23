#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMerchantcardOpenCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardOpenCreateResponse, self).__init__()
        self._fail_reason = None
        self._submit_result = None

    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def submit_result(self):
        return self._submit_result

    @submit_result.setter
    def submit_result(self, value):
        self._submit_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardOpenCreateResponse, self).parse_response_content(response_content)
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'submit_result' in response:
            self.submit_result = response['submit_result']
