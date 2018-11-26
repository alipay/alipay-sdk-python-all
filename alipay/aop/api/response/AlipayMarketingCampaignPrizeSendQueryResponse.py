#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PrizeDetail import PrizeDetail


class AlipayMarketingCampaignPrizeSendQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignPrizeSendQueryResponse, self).__init__()
        self._prize_detail_list = None

    @property
    def prize_detail_list(self):
        return self._prize_detail_list

    @prize_detail_list.setter
    def prize_detail_list(self, value):
        if isinstance(value, list):
            self._prize_detail_list = list()
            for i in value:
                if isinstance(i, PrizeDetail):
                    self._prize_detail_list.append(i)
                else:
                    self._prize_detail_list.append(PrizeDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignPrizeSendQueryResponse, self).parse_response_content(response_content)
        if 'prize_detail_list' in response:
            self.prize_detail_list = response['prize_detail_list']
