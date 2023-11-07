#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignPlaysigninCountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignPlaysigninCountQueryResponse, self).__init__()
        self._continuous_num = None
        self._cumulative_num = None

    @property
    def continuous_num(self):
        return self._continuous_num

    @continuous_num.setter
    def continuous_num(self, value):
        self._continuous_num = value
    @property
    def cumulative_num(self):
        return self._cumulative_num

    @cumulative_num.setter
    def cumulative_num(self, value):
        self._cumulative_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignPlaysigninCountQueryResponse, self).parse_response_content(response_content)
        if 'continuous_num' in response:
            self.continuous_num = response['continuous_num']
        if 'cumulative_num' in response:
            self.cumulative_num = response['cumulative_num']
