#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PaymentAbilityPostbackResponse import PaymentAbilityPostbackResponse


class AlipayDatabizCorePaymentAbilityUpdateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDatabizCorePaymentAbilityUpdateResponse, self).__init__()
        self._payment_ability_postback_response = None

    @property
    def payment_ability_postback_response(self):
        return self._payment_ability_postback_response

    @payment_ability_postback_response.setter
    def payment_ability_postback_response(self, value):
        if isinstance(value, PaymentAbilityPostbackResponse):
            self._payment_ability_postback_response = value
        else:
            self._payment_ability_postback_response = PaymentAbilityPostbackResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDatabizCorePaymentAbilityUpdateResponse, self).parse_response_content(response_content)
        if 'payment_ability_postback_response' in response:
            self.payment_ability_postback_response = response['payment_ability_postback_response']
