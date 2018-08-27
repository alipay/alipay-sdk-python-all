#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCardBenefitCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCardBenefitCreateResponse, self).__init__()
        self._benefit_id = None

    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCardBenefitCreateResponse, self).parse_response_content(response_content)
        if 'benefit_id' in response:
            self.benefit_id = response['benefit_id']
