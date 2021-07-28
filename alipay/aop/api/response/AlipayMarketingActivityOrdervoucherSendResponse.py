#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingActivityOrdervoucherSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityOrdervoucherSendResponse, self).__init__()
        self._voucher_code = None

    @property
    def voucher_code(self):
        return self._voucher_code

    @voucher_code.setter
    def voucher_code(self, value):
        self._voucher_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityOrdervoucherSendResponse, self).parse_response_content(response_content)
        if 'voucher_code' in response:
            self.voucher_code = response['voucher_code']
