#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantMemberwalletWithdrawSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantMemberwalletWithdrawSubmitResponse, self).__init__()
        self._actual_withdraw_amount = None
        self._withdraw_amount = None

    @property
    def actual_withdraw_amount(self):
        return self._actual_withdraw_amount

    @actual_withdraw_amount.setter
    def actual_withdraw_amount(self, value):
        self._actual_withdraw_amount = value
    @property
    def withdraw_amount(self):
        return self._withdraw_amount

    @withdraw_amount.setter
    def withdraw_amount(self, value):
        self._withdraw_amount = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantMemberwalletWithdrawSubmitResponse, self).parse_response_content(response_content)
        if 'actual_withdraw_amount' in response:
            self.actual_withdraw_amount = response['actual_withdraw_amount']
        if 'withdraw_amount' in response:
            self.withdraw_amount = response['withdraw_amount']
