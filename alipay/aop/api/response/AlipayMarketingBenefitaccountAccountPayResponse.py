#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingBenefitaccountAccountPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingBenefitaccountAccountPayResponse, self).__init__()
        self._order_no = None
        self._pc_payment_url = None
        self._recharge_no = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def pc_payment_url(self):
        return self._pc_payment_url

    @pc_payment_url.setter
    def pc_payment_url(self, value):
        self._pc_payment_url = value
    @property
    def recharge_no(self):
        return self._recharge_no

    @recharge_no.setter
    def recharge_no(self, value):
        self._recharge_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingBenefitaccountAccountPayResponse, self).parse_response_content(response_content)
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'pc_payment_url' in response:
            self.pc_payment_url = response['pc_payment_url']
        if 'recharge_no' in response:
            self.recharge_no = response['recharge_no']
