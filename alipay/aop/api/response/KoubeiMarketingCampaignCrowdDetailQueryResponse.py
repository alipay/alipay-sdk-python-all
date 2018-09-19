#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingCampaignCrowdDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignCrowdDetailQueryResponse, self).__init__()
        self._crowd_group_info = None
        self._name = None

    @property
    def crowd_group_info(self):
        return self._crowd_group_info

    @crowd_group_info.setter
    def crowd_group_info(self, value):
        self._crowd_group_info = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignCrowdDetailQueryResponse, self).parse_response_content(response_content)
        if 'crowd_group_info' in response:
            self.crowd_group_info = response['crowd_group_info']
        if 'name' in response:
            self.name = response['name']
