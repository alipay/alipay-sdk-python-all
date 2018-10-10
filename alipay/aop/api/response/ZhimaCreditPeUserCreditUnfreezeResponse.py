#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeUserCreditUnfreezeResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeUserCreditUnfreezeResponse, self).__init__()
        self._amount = None
        self._out_request_no = None
        self._success = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeUserCreditUnfreezeResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'success' in response:
            self.success = response['success']
