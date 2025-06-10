#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingBenefitaccountAccountCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingBenefitaccountAccountCreateResponse, self).__init__()
        self._benefit_account_no = None

    @property
    def benefit_account_no(self):
        return self._benefit_account_no

    @benefit_account_no.setter
    def benefit_account_no(self, value):
        self._benefit_account_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingBenefitaccountAccountCreateResponse, self).parse_response_content(response_content)
        if 'benefit_account_no' in response:
            self.benefit_account_no = response['benefit_account_no']
