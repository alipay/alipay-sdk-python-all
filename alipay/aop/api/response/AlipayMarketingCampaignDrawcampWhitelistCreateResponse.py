#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignDrawcampWhitelistCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignDrawcampWhitelistCreateResponse, self).__init__()
        self._camp_result = None

    @property
    def camp_result(self):
        return self._camp_result

    @camp_result.setter
    def camp_result(self, value):
        self._camp_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignDrawcampWhitelistCreateResponse, self).parse_response_content(response_content)
        if 'camp_result' in response:
            self.camp_result = response['camp_result']
