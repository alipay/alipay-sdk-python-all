#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceAssetRepaymentProveResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceAssetRepaymentProveResponse, self).__init__()
        self._accepted = None
        self._error_code = None
        self._error_msg = None

    @property
    def accepted(self):
        return self._accepted

    @accepted.setter
    def accepted(self, value):
        self._accepted = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceAssetRepaymentProveResponse, self).parse_response_content(response_content)
        if 'accepted' in response:
            self.accepted = response['accepted']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
