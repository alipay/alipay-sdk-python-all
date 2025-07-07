#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingBenefitaccountAccountRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingBenefitaccountAccountRefundResponse, self).__init__()
        self._amount = None
        self._order_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingBenefitaccountAccountRefundResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'order_no' in response:
            self.order_no = response['order_no']
