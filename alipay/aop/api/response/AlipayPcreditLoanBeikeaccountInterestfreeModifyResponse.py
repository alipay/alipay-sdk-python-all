#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BeikeAccountResponse import BeikeAccountResponse


class AlipayPcreditLoanBeikeaccountInterestfreeModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanBeikeaccountInterestfreeModifyResponse, self).__init__()
        self._beike_account_response = None

    @property
    def beike_account_response(self):
        return self._beike_account_response

    @beike_account_response.setter
    def beike_account_response(self, value):
        if isinstance(value, BeikeAccountResponse):
            self._beike_account_response = value
        else:
            self._beike_account_response = BeikeAccountResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanBeikeaccountInterestfreeModifyResponse, self).parse_response_content(response_content)
        if 'beike_account_response' in response:
            self.beike_account_response = response['beike_account_response']
