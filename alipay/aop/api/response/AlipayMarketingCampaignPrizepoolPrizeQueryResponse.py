#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PrizeConfig import PrizeConfig


class AlipayMarketingCampaignPrizepoolPrizeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignPrizepoolPrizeQueryResponse, self).__init__()
        self._prize_config = None

    @property
    def prize_config(self):
        return self._prize_config

    @prize_config.setter
    def prize_config(self, value):
        if isinstance(value, PrizeConfig):
            self._prize_config = value
        else:
            self._prize_config = PrizeConfig.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignPrizepoolPrizeQueryResponse, self).parse_response_content(response_content)
        if 'prize_config' in response:
            self.prize_config = response['prize_config']
