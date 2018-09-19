#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PaymentAbilityQueryResponse import PaymentAbilityQueryResponse


class AlipayDatabizCorePaymentAbilityGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDatabizCorePaymentAbilityGetResponse, self).__init__()
        self._payment_ability_query_response = None

    @property
    def payment_ability_query_response(self):
        return self._payment_ability_query_response

    @payment_ability_query_response.setter
    def payment_ability_query_response(self, value):
        if isinstance(value, PaymentAbilityQueryResponse):
            self._payment_ability_query_response = value
        else:
            self._payment_ability_query_response = PaymentAbilityQueryResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDatabizCorePaymentAbilityGetResponse, self).parse_response_content(response_content)
        if 'payment_ability_query_response' in response:
            self.payment_ability_query_response = response['payment_ability_query_response']
