#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceZhimaSubmerchantQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceZhimaSubmerchantQueryResponse, self).__init__()
        self._fail_reason = None
        self._status = None

    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceZhimaSubmerchantQueryResponse, self).parse_response_content(response_content)
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'status' in response:
            self.status = response['status']
