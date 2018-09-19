#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RechargeBill import RechargeBill


class AlipayCommerceCityfacilitatorDepositQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCityfacilitatorDepositQueryResponse, self).__init__()
        self._recharge_bills = None

    @property
    def recharge_bills(self):
        return self._recharge_bills

    @recharge_bills.setter
    def recharge_bills(self, value):
        if isinstance(value, list):
            self._recharge_bills = list()
            for i in value:
                if isinstance(i, RechargeBill):
                    self._recharge_bills.append(i)
                else:
                    self._recharge_bills.append(RechargeBill.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCityfacilitatorDepositQueryResponse, self).parse_response_content(response_content)
        if 'recharge_bills' in response:
            self.recharge_bills = response['recharge_bills']
