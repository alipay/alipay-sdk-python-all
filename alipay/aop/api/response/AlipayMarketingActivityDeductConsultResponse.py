#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingActivityDeductConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityDeductConsultResponse, self).__init__()
        self._optimal_total_promo_amount = None

    @property
    def optimal_total_promo_amount(self):
        return self._optimal_total_promo_amount

    @optimal_total_promo_amount.setter
    def optimal_total_promo_amount(self, value):
        self._optimal_total_promo_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityDeductConsultResponse, self).parse_response_content(response_content)
        if 'optimal_total_promo_amount' in response:
            self.optimal_total_promo_amount = response['optimal_total_promo_amount']
