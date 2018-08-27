#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingCampaignCrowdCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignCrowdCreateResponse, self).__init__()
        self._crowd_group_id = None

    @property
    def crowd_group_id(self):
        return self._crowd_group_id

    @crowd_group_id.setter
    def crowd_group_id(self, value):
        self._crowd_group_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignCrowdCreateResponse, self).parse_response_content(response_content)
        if 'crowd_group_id' in response:
            self.crowd_group_id = response['crowd_group_id']
