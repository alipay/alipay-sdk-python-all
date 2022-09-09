#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantMemberwalletReturnSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantMemberwalletReturnSubmitResponse, self).__init__()
        self._actual_return_amount = None
        self._return_amount = None

    @property
    def actual_return_amount(self):
        return self._actual_return_amount

    @actual_return_amount.setter
    def actual_return_amount(self, value):
        self._actual_return_amount = value
    @property
    def return_amount(self):
        return self._return_amount

    @return_amount.setter
    def return_amount(self, value):
        self._return_amount = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantMemberwalletReturnSubmitResponse, self).parse_response_content(response_content)
        if 'actual_return_amount' in response:
            self.actual_return_amount = response['actual_return_amount']
        if 'return_amount' in response:
            self.return_amount = response['return_amount']
