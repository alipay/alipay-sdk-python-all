#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupFundUserBill import GroupFundUserBill


class AlipayFundTransGroupfundsUserbillsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransGroupfundsUserbillsQueryResponse, self).__init__()
        self._user_bills = None

    @property
    def user_bills(self):
        return self._user_bills

    @user_bills.setter
    def user_bills(self, value):
        if isinstance(value, GroupFundUserBill):
            self._user_bills = value
        else:
            self._user_bills = GroupFundUserBill.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransGroupfundsUserbillsQueryResponse, self).parse_response_content(response_content)
        if 'user_bills' in response:
            self.user_bills = response['user_bills']
