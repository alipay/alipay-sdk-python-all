#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignPrizeAmountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignPrizeAmountQueryResponse, self).__init__()
        self._remain_amount = None

    @property
    def remain_amount(self):
        return self._remain_amount

    @remain_amount.setter
    def remain_amount(self, value):
        self._remain_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignPrizeAmountQueryResponse, self).parse_response_content(response_content)
        if 'remain_amount' in response:
            self.remain_amount = response['remain_amount']
