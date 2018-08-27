#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PrizeModel import PrizeModel


class MybankMarketingCampaignPrizeListQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankMarketingCampaignPrizeListQueryResponse, self).__init__()
        self._prize_list = None
        self._total_size = None

    @property
    def prize_list(self):
        return self._prize_list

    @prize_list.setter
    def prize_list(self, value):
        if isinstance(value, list):
            self._prize_list = list()
            for i in value:
                if isinstance(i, PrizeModel):
                    self._prize_list.append(i)
                else:
                    self._prize_list.append(PrizeModel.from_alipay_dict(i))
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(MybankMarketingCampaignPrizeListQueryResponse, self).parse_response_content(response_content)
        if 'prize_list' in response:
            self.prize_list = response['prize_list']
        if 'total_size' in response:
            self.total_size = response['total_size']
