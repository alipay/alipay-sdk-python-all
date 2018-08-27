#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignActivityOfflineCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignActivityOfflineCreateResponse, self).__init__()
        self._camp_id = None
        self._prize_id = None

    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignActivityOfflineCreateResponse, self).parse_response_content(response_content)
        if 'camp_id' in response:
            self.camp_id = response['camp_id']
        if 'prize_id' in response:
            self.prize_id = response['prize_id']
