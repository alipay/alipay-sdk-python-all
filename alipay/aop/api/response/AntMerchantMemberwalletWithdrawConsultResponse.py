#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantMemberwalletWithdrawConsultResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantMemberwalletWithdrawConsultResponse, self).__init__()
        self._actual_available_withdraw_amount = None
        self._available_withdraw_amount = None

    @property
    def actual_available_withdraw_amount(self):
        return self._actual_available_withdraw_amount

    @actual_available_withdraw_amount.setter
    def actual_available_withdraw_amount(self, value):
        self._actual_available_withdraw_amount = value
    @property
    def available_withdraw_amount(self):
        return self._available_withdraw_amount

    @available_withdraw_amount.setter
    def available_withdraw_amount(self, value):
        self._available_withdraw_amount = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantMemberwalletWithdrawConsultResponse, self).parse_response_content(response_content)
        if 'actual_available_withdraw_amount' in response:
            self.actual_available_withdraw_amount = response['actual_available_withdraw_amount']
        if 'available_withdraw_amount' in response:
            self.available_withdraw_amount = response['available_withdraw_amount']
