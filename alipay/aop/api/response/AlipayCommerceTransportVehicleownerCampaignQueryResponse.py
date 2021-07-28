#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MarketInfo import MarketInfo


class AlipayCommerceTransportVehicleownerCampaignQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportVehicleownerCampaignQueryResponse, self).__init__()
        self._market_info = None

    @property
    def market_info(self):
        return self._market_info

    @market_info.setter
    def market_info(self, value):
        if isinstance(value, MarketInfo):
            self._market_info = value
        else:
            self._market_info = MarketInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportVehicleownerCampaignQueryResponse, self).parse_response_content(response_content)
        if 'market_info' in response:
            self.market_info = response['market_info']
