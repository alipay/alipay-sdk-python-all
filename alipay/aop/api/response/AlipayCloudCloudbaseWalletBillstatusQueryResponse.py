#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseWalletBillstatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseWalletBillstatusQueryResponse, self).__init__()
        self._bill_amount = None
        self._origin_bill_amount = None
        self._result = None

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def origin_bill_amount(self):
        return self._origin_bill_amount

    @origin_bill_amount.setter
    def origin_bill_amount(self, value):
        self._origin_bill_amount = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseWalletBillstatusQueryResponse, self).parse_response_content(response_content)
        if 'bill_amount' in response:
            self.bill_amount = response['bill_amount']
        if 'origin_bill_amount' in response:
            self.origin_bill_amount = response['origin_bill_amount']
        if 'result' in response:
            self.result = response['result']
