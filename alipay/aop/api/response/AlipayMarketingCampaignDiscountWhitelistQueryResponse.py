#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignDiscountWhitelistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignDiscountWhitelistQueryResponse, self).__init__()
        self._camp_id = None
        self._user_white_list = None

    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def user_white_list(self):
        return self._user_white_list

    @user_white_list.setter
    def user_white_list(self, value):
        self._user_white_list = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignDiscountWhitelistQueryResponse, self).parse_response_content(response_content)
        if 'camp_id' in response:
            self.camp_id = response['camp_id']
        if 'user_white_list' in response:
            self.user_white_list = response['user_white_list']
