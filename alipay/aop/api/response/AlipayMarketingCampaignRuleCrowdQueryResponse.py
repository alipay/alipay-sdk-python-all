#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignRuleCrowdQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignRuleCrowdQueryResponse, self).__init__()
        self._scenetagjson = None

    @property
    def scenetagjson(self):
        return self._scenetagjson

    @scenetagjson.setter
    def scenetagjson(self, value):
        self._scenetagjson = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignRuleCrowdQueryResponse, self).parse_response_content(response_content)
        if 'scenetagjson' in response:
            self.scenetagjson = response['scenetagjson']
