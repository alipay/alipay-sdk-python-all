#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommercePayforprivilegeBalanceWithdrawResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePayforprivilegeBalanceWithdrawResponse, self).__init__()
        self._withdraw_id = None

    @property
    def withdraw_id(self):
        return self._withdraw_id

    @withdraw_id.setter
    def withdraw_id(self, value):
        self._withdraw_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommercePayforprivilegeBalanceWithdrawResponse, self).parse_response_content(response_content)
        if 'withdraw_id' in response:
            self.withdraw_id = response['withdraw_id']
