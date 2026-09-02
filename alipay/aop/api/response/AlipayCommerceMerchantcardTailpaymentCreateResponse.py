#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMerchantcardTailpaymentCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardTailpaymentCreateResponse, self).__init__()
        self._tail_payment_id = None
        self._tail_payment_order_pay_url = None

    @property
    def tail_payment_id(self):
        return self._tail_payment_id

    @tail_payment_id.setter
    def tail_payment_id(self, value):
        self._tail_payment_id = value
    @property
    def tail_payment_order_pay_url(self):
        return self._tail_payment_order_pay_url

    @tail_payment_order_pay_url.setter
    def tail_payment_order_pay_url(self, value):
        self._tail_payment_order_pay_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardTailpaymentCreateResponse, self).parse_response_content(response_content)
        if 'tail_payment_id' in response:
            self.tail_payment_id = response['tail_payment_id']
        if 'tail_payment_order_pay_url' in response:
            self.tail_payment_order_pay_url = response['tail_payment_order_pay_url']
