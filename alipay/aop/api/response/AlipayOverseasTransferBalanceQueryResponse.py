#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Money import Money


class AlipayOverseasTransferBalanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTransferBalanceQueryResponse, self).__init__()
        self._balances = None
        self._pass_through_info = None

    @property
    def balances(self):
        return self._balances

    @balances.setter
    def balances(self, value):
        if isinstance(value, list):
            self._balances = list()
            for i in value:
                if isinstance(i, Money):
                    self._balances.append(i)
                else:
                    self._balances.append(Money.from_alipay_dict(i))
    @property
    def pass_through_info(self):
        return self._pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self._pass_through_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTransferBalanceQueryResponse, self).parse_response_content(response_content)
        if 'balances' in response:
            self.balances = response['balances']
        if 'pass_through_info' in response:
            self.pass_through_info = response['pass_through_info']
