#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserPrivilegerecordQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserPrivilegerecordQueryResponse, self).__init__()
        self._privilege_usage_status = None
        self._voucher_code = None

    @property
    def privilege_usage_status(self):
        return self._privilege_usage_status

    @privilege_usage_status.setter
    def privilege_usage_status(self, value):
        self._privilege_usage_status = value
    @property
    def voucher_code(self):
        return self._voucher_code

    @voucher_code.setter
    def voucher_code(self, value):
        self._voucher_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserPrivilegerecordQueryResponse, self).parse_response_content(response_content)
        if 'privilege_usage_status' in response:
            self.privilege_usage_status = response['privilege_usage_status']
        if 'voucher_code' in response:
            self.voucher_code = response['voucher_code']
