#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingBenefitaccountAccountCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingBenefitaccountAccountCreateResponse, self).__init__()
        self._benefit_account_no = None
        self._out_card_no = None

    @property
    def benefit_account_no(self):
        return self._benefit_account_no

    @benefit_account_no.setter
    def benefit_account_no(self, value):
        self._benefit_account_no = value
    @property
    def out_card_no(self):
        return self._out_card_no

    @out_card_no.setter
    def out_card_no(self, value):
        self._out_card_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingBenefitaccountAccountCreateResponse, self).parse_response_content(response_content)
        if 'benefit_account_no' in response:
            self.benefit_account_no = response['benefit_account_no']
        if 'out_card_no' in response:
            self.out_card_no = response['out_card_no']
